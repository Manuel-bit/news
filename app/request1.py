import urllib.request,json
from .models import Article,Sources
from config import Config

source_url = Config.SOURCE_URL

def fetchSources():
  '''
  function that fetches news Sources from nes api
  '''
  with urllib.request.urlopen(source_url+'281dbdc2e10e4a6ab51a9a27a614c146')as url:
    source_data = url.read()
    source_response = json.loads(source_data)

    source_results = None

    if source_response['sources']:
      source_result_list = source_response['sources']
      source_results = process_results(source_result_list)
        
  return source_results
    
    
    

def process_results(source_list):

  source_results = []
  for sources in source_list:
    id =  sources.get('id')
    name = sources.get('name')
    description = sources.get('description')
    url = sources.get('url')
    category = sources.get('category')
    language = sources.get('language')

    if language == 'en':
      source_object = Sources(id,name,description,url,category,language)
      source_results.append(source_object)

  return source_results