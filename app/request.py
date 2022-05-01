from app import News
import urllib.request,json
from .models import articles,source

Article=articles.Article
Source=source.Source

api_key=News.config['NEWS_API_KEY']

base_url=News.config['NEWS_API_BASE_URL']

source_url=News.config['NEWS_API_SOURCE_URL']

def get_news(category):

    get_news_url=base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url)as url:
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

def get_category(cat_name):
    '''
    function that gets the response to the category json
    '''
    get_category_url = base_url.format(cat_name,api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_results(get_cartegory_list)

    return get_cartegory_results   

# def category(cat_name):
#     """
#     Function that gets response from the json

#     """