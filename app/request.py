# from app import app
import urllib.request,json
from .models import *


# Article=models.Article
# Source=models.Source

# api_key=app.config['NEWS_API_KEY']

# base_url=app.config['NEWS_API_BASE_URL']

# source_url=app.config['NEWS_API_SOURCE_URL']
api_key = None
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key=app.config['NEWS_API_KEY']

    base_url=app.config['NEWS_API_BASE_URL'] 

    source_url=app.config['NEWS_API_SOURCE_URL']

    pass

    
def get_news(category):

    get_news_url=base_url.format(category,api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_article_data=url.read()
        get_news_response=json.loads(get_article_data)#convert to python dictionary

        news_results=None

        if get_news_response['articles']:
            news_results_list=get_news_response['articles']
            news_results=process_results(news_results_list)

    return news_results

def process_results(news_list):

    news_results=[]
    for item in news_list:
        id=item.get('id')
        title=item.get('title')
        description=item.get('description')
        author=item.get('author')
        url=item.get('url')
        urlToImage=item.get('urlToImage')
        publishedAt=item.get('publishedAt')

        if description:
            news_object=Article(id,title,description,url,author,urlToImage,publishedAt)
            news_results.append(news_object)

    return news_results

def get_source():
    get_source_url=source_url.format(id,api_key)

    with urllib.request.urlopen(get_source_url)as url:
        get_source_data=url.read()
        get_source_response=json.loads(get_source_data)#convert to python dictionary

        source_results=None

        if get_source_response['sources']:
            source_results_list=get_source_response['sources']
            source_results=output_results(source_results_list)

    return source_results

def output_results(source_list):

    source_results=[]
    for item in source_list:
        id=item.get('id')
        name=item.get('name')
        description=item.get('description')
        url=item.get('url')

        if description:
            source_object=Source(id,name,description,url)
            source_results.append(source_object)

    return source_results

def get_category(cate_name):
    '''
    Function that gets the response 
    '''
    get_category_url = base_url.format(cate_name,api_key)
    # print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        get_category_results = None

        if get_category_response['articles']:
            get_category_list = get_category_response['articles']
            get_category_results = process_results(get_category_list)

    return get_category_results   

