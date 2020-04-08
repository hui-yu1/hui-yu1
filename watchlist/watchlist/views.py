from watchlist import app,db
from flask import Flask,url_for,render_template,request,redirect,flash
from flask_login import logout_user,login_user,login_required,current_user
from watchlist.models import User,Movie


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