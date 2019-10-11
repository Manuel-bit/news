import urllib.request,json
from .models import Article,Sources
from config import Config

news_url = Config.NEWS_URL
source_url = Config.SOURCE_URL

def getHeadlines():
  '''
  function that gets json response
  '''
  with urllib.request.urlopen(news_url+'281dbdc2e10e4a6ab51a9a27a614c146')as url:
    headlines_data = url.read()
    headlines_response = json.loads(headlines_data)

    headlines_results = None

    if headlines_response['articles']:
      headlines_results_list = headlines_response['articles']
      headlines_results = process_results(headlines_results_list)

  return headlines_results

def process_results(headlines_list):

  headlines_result = []
  for headlines in headlines_list:
    author = headlines.get('author')
    title = headlines.get('title')
    description = headlines.get('description')
    url = headlines.get('url')
    urlToImage = headlines.get('urlToImage')
    publishedAt = headlines.get('publishedAt')

    if title:
      headline_object = Article(author,title,description,url,urlToImage,publishedAt)
      headlines_result.append(headline_object)

  return headlines_result


# def fetchSources():
#   '''
#   function that fetches news Sources from nes api
#   '''
#   with urllib.request.urlopen(source_url+'281dbdc2e10e4a6ab51a9a27a614c146')as url:
#     source_data = url.read()
#     source_response = json.loads(source_data)

#     source_results = None

#     if source_response['sources']:
#       source_result_list = source_response['sources']
#       source_results = process_results(source_result_list)
       
#   return source_results

# def process_results(source_list):

#   source_result = []
#   for sources in source_list:
#     id =  sources.get('id')
#     name = sources.get('name')
#     description = sources.get('description')
#     url = sources.get('url')
#     category = sources.get('category')
#     language = sources.get('language')

#     if language:
#       source_object = Sources(id,name,description,url,category,language)
#       source_result.append(source_object)

#   return source_result



