from flask import render_template
from app import News
from .request import get_news



@News.route('/')
def index():
    health_news=get_news('health')
    sport_news=get_news('sports')
    breaking_news=get_news('breaking')
    entertainment_news=get_news('entertainment')
    return render_template('index.html', health=health_news,sports=sport_news,breaking=breaking_news,entertainment=entertainment_news)