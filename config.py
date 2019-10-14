import os

class Config:
  '''
  class that contains general configuarations
  '''
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey='
  SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey='
  NEWS_URL = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey='

class ProdConfig(Config):
  '''
  class that contain configuarations during production
  '''
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  DEBUG = False
class DevConfig(Config):
  '''
  class that contains configuarations during development
  '''
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  DEBUG = True

config_options ={
  'production'  : ProdConfig,
  'development' : DevConfig
}