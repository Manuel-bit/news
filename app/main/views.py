from flask import render_template
from . import main
from app.requests import getHeadlines,getNews
from app.request1 import fetchSources
import datetime


@main.route('/')
def index():
  ww = getNews()
  print(ww)
  title = "All News"
  return render_template('index.html',ww=ww,title=title)

@main.route('/sources')
def sources():
  title = "News Sources"
  source = fetchSources()
  return render_template('sources.html',title=title,source=source)

@main.route('/highlights')
def highlights():
  headlines = getHeadlines()
  title = "News Highlights"
  return render_template('highlights.html',headlines=headlines,title=title)