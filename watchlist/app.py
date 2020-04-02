
from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'lion'
    movies = [
        {"title":"萨霍","year":"2019"},
        {"title":"星游记","year":"2020"},
        {"title":"急速备战","year":"2019"},
        {"title":"叶问4","year":"2019"},
        {"title":"三人行","year":"2016"},
    ]
    return render_template('index.html',name=name,movies=movies)