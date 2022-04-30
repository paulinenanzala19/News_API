from app import News
import urllib.request,json
from .models import news

Article=news.Article

api_key=News.config['NEWS_API_KEY']

base_url=News.config['NEWS_API_BASE_URL']

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

        if description:
            news_object=Article(id,title,description,url,author)
            news_results.append(news_object)

    return news_results