import os,sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

db = SQLAlchemy(app)

WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///"  # windows平台
else:
    prefix = "sqlite:////"  # Mac,Linux平台

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path),'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


login_manager = LoginManager(app) # 实例化扩展类
@login_manager.user_loader
def load_user(user_id): # 创建用户加载回调函数，接受用户ID作为参数
    from watchlist.models import User
    user = User.query.get(int(user_id))
    return user

login_manager.login_view = 'login'
login_manager.login_message = '尚未登录'

# 模板上下文处理函数
@app.context_processor
def common_user():
    from watchlist.models import User
    user = User.query.filter()  # 筛选出用户记录
    return dict(user=user)

from watchlist import views,errors,commands
