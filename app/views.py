from flask import render_template
from app import News
from .request import get_news,get_source,get_category




@News.route('/')
def index():
    """

    """
   
    health_news=get_news('health')
    sport_news=get_news('sports')
    entertainment_news=get_news('entertainment')
    return render_template('index.html', health=health_news,sports=sport_news,
    entertainment=entertainment_news)


@News.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name

    return render_template('categories.html',title = title,category = category, cat= cat_name)

