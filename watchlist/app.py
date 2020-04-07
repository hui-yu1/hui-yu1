import os,sys

from flask import Flask,url_for,render_template,request,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin,logout_user,login_user,login_required,current_user

import click

WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///"  # windows平台
else:
    prefix = "sqlite:////"  # Mac,Linux平台

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1903_dev'

db = SQLAlchemy(app)

login_manager = LoginManager(app) # 实例化扩展类
@login_manager.user_loader
def load_user(user_id): # 创建用户加载回调函数，接受用户ID作为参数
    user = User.query.get(int(user_id))
    return user

login_manager.login_view = 'login'
login_manager.login_message = '尚未登录'

# models 数据库
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    def validate_password(self,password):
        return check_password_hash(self.password_hash,password)

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(30))


# views视图函数
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
        # 获取表单内容
        title = request.form.get('title')
        year = request.form.get('year')
        # 验证数据
        if not title or not year or len(year)>4 or len(title)>60:
            flash("输入错误")
            return redirect(url_for('index'))
        # 将数据存入数据库
        movie = Movie(title=title,year=year)
        db.session.add(movie)
        db.session.commit()
        flash("添加成功")
        return redirect(url_for('index'))
    movies = Movie.query.all() 
    return render_template('index.html',movies=movies)

# 编辑页面
@app.route('/movie/edit/<int:movie_id>',methods=['GET','POST'])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        # 验证数据
        if not title or not year or len(year)>4 or len(title)>60:
            flash("输入错误")
            return redirect(url_for('edit'),movie_id=movie_id)
        # 将数据存入数据库
        movie.title = title
        movie.year = year
        db.session.commit()
        flash("编辑成功")
        return redirect(url_for('index'))
    return render_template('edit.html',movie=movie)

# 删除视图函数
@app.route('/movie/delete/<int:movie_id>',methods=['GET','POST'])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('删除成功')
    return redirect(url_for('index'))

# 登录
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            flash('输入错误')
            return redirect(url_for('login'))
        user = User.query.first()
        # 验证用户名密码是否一致
        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('登录成功')
            return redirect(url_for('index'))
        flash('用户名或密码错误')
        return redirect(url_for('login'))
    return render_template('login.html')

# 登出
@app.route('/logout')
def logout():
    logout_user()
    flash('退出')
    return redirect(url_for('index'))

# 设置
@app.route('/settings',methods=['GET','POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name or len(name)>20:
            flash('输入有误')
            return redirect(url_for('index'))
        current_user.name = name
        db.session.commit()
        flash('更改成功')
        return redirect(url_for('index'))

    return render_template('settings.html')

# 自定义命令
@app.cli.command()  # 注册为命令
@click.option('--drop',is_flag=True,help="先删除再创建")
def initdb(drop):
    if drop:
        db.drop_all()
        click.echo("删除成功")
    db.create_all()
    click.echo("初始化数据库完成")

# 向数据库中插入数据
@app.cli.command()
def forge():
    name = 'lion'
    movies = [
        {"title":"萨霍","year":"2019"},
        {"title":"星游记","year":"2020"},
        {"title":"急速备战","year":"2019"},
        {"title":"叶问4","year":"2019"},
        {"title":"三人行","year":"2016"},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo("导入数据完成")

# 自定义指令，生成管理员账号flask admin
# 输入用户名Admin,密码，确认密码
@app.cli.command()
@click.option('--username',prompt=True,help='登录用户名')
@click.option('--password',prompt=True,help='登录密码',confirmation_prompt=True,hide_input=True)
def admin(username,password):
    user = User.query.first()
    if user is not None:
        click.echo('更新管理员用户')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建管理员账户')
        user = User(username=username,name='Admin')
        user.set_password(password)
        db.session.add(user)
    
    db.session.commit()
    click.echo('管理员账户更新/创建完成')

# 错误处理函数
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

# 模板上下文处理函数
@app.context_processor
def common_user():
    user = User.query.filter()  # 筛选出用户记录
    return dict(user=user)


