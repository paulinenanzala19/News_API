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
        get_news_response=json.load(get_article_data)#convert to python dictionary

        news_results=None

        if get_news_response['results']:
            news_results_list=get_news_response['results']
            news_results=process_results(news_results_list)

    return news_results