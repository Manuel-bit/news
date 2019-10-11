class Config:
  '''
  class that contains general configuarations
  '''
  NEWS_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey='
  SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey='

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