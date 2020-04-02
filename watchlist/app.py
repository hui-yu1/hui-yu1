# import os,sys

from flask import Flask,url_for,render_template
# from flask_sqlalchemy import SQLAlchemy

# import click

# WIN = sys.platform.startswith('win')
# if WIN:
#     prefix = "sqlite:///"  # windows平台
# else:
#     prefix = "sqlite:////"  # Mac,Linux平台

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = prefix + "sqlite:///" + os.path.join(app.root_path,'data.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # models 数据库
# class User(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(20))

# class Movie(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     title = db.Column(db.String(60))
#     year = db.Column(db.String(30))


# views视图函数
@app.route('/')
def index():
    return "yes"
#     name = 'lion'
#     movies = [
#         {"title":"萨霍","year":"2019"},
#         {"title":"星游记","year":"2020"},
#         {"title":"急速备战","year":"2019"},
#         {"title":"叶问4","year":"2019"},
#         {"title":"三人行","year":"2016"},
#     ]
#     return render_template('index.html',name=name,movies=movies)


# 自定义命令
# @app.cli.command()  # 注册为命令
# @click.option('--drop',is_flag=True,help="先删除再创建")
# def initdb(drop):
#     if drop:
#         db.drop_all()
#     db.create_all()
#     click.echo("初始化数据库完成")


