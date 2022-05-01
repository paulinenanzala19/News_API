from flask import render_template
from app import News
from .request import get_news,get_source,get_category




@News.route('/')
def index():
    """

    """
    general_news=get_news('general')
    # health_news=get_news('health')
    # sport_news=get_news('sports')
    # entertainment_news=get_news('entertainment')
    return render_template('index.html',general=general_news)


@News.route('/categories/<cate_name>')
def category(cate_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cate_name)
    title = f'{cate_name}'
    cate = cate_name

    return render_template('categories.html',title = title,category = category, cate= cate_name)

