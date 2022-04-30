from flask import render_template
from app import News
from .request import get_news



@News.route('/')
def index():
    health_news=get_news('health')
    return render_template('index.html', health=health_news)