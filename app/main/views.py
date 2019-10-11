from flask import render_template
from . import main
from app.requests import getHeadlines


@main.route('/')
def index():
  headlines = getHeadlines()
  print(headlines)
  return render_template('index.html',headlines=headlines)

@main.route('/sources')
def sources():
  
  return render_template('sources.html')
