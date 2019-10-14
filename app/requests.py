import urllib.request,json
from .models import Article,Sources
from config import Config

headlines_url = Config.HEADLINES_URL
source_url = Config.SOURCE_URL
news_url = Config.NEWS_URL
news_api = Config.NEWS_API_KEY

def getHeadlines():
  '''
  function that gets json response
  '''
  with urllib.request.urlopen(headlines_url+news_api)as url:
    headlines_data = url.read()
    headlines_response = json.loads(headlines_data)

    headlines_results = None

    if headlines_response['articles']:
      headlines_results_list = headlines_response['articles']
      headlines_results = process_results(headlines_results_list)

  return headlines_results

def process_results(headlines_list):

  headlines_results = []
  for headlines in headlines_list:
    author = headlines.get('author')
    title = headlines.get('title')
    description = headlines.get('description')
    url = headlines.get('url')
    urlToImage = headlines.get('urlToImage')
    publishedAt = headlines.get('publishedAt')

    if title:
      headline_object = Article(author,title,description,url,urlToImage,publishedAt)
      headlines_results.append(headline_object)

  return headlines_results




def getNews():
  '''
  function that fetches all news
  '''

  with urllib.request.urlopen(news_url+news_api) as url:
    news_data = url.read()
    news_response = json.loads(news_data)

    all_news = None

    if news_response['articles']:
      all_news_list = news_response['articles']
      all_news_data = process_news(all_news_list)

  return all_news_data

def process_news(news_list):
  
  all_news_data = []
  for news in news_list:
    author = news.get('author')
    title = news.get('title')
    description = news.get('description')
    url = news.get('url')
    urlToImage = news.get('urlToImage')
    publishedAt = news.get('publishedAt')

    if title:
      news_object = Article(author,title,description,url,urlToImage,publishedAt)
      all_news_data.append(news_object)

  return all_news_data
