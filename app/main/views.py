from flask import render_template
from . import main
from app.requests import getHeadlines,getNews
from app.request1 import fetchSources


@main.route('/')
def index():
  news = getNews()
  title = "All News"
  return render_template('index.html',news=news,title=title)

@main.route('/sources')
def sources():
  title = "News Sources"
  source = fetchSources()
  print(source)
  return render_template('sources.html',title=title,source=source)

@main.route('/highlights')
def highlights():
  headlines = getHeadlines()
  title = "News Highlights"
  return render_template('highlights.html',headlines=headlines,title=title)