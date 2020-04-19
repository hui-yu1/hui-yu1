from watchlist import app,db
from flask import Flask,url_for,render_template,request,redirect,flash
from flask_login import logout_user,login_user,login_required,current_user
from watchlist.models import User,Movie




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