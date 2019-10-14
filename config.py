

class Config:
  '''
  class that contains general configuarations
  '''
  HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey='
  SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey='
  NEWS_URL = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey='

class ProdConfig(Config):
  '''
  class that contain configuarations during production
  '''
  pass
class DevConfig(Config):
  '''
  class that contains configuarations during development
  '''
  DEBUG = True

config_options ={
  'production'  : ProdConfig,
  'development' : DevConfig
}