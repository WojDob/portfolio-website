import json
import urllib.request

from django.shortcuts import render

# Create your views here.
def index(request, source='new-scientist'):
    apikey = '5d6ed3545a734b53bb70ce1361ae80f3'
    url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(source, apikey)
    handle = urllib.request.urlopen(url)
    string = handle.read().decode()
    data = json.loads(string)
    handle.close()
    context = {
      'newsapi': data,
      'sources': [
        ('ars-technica', 'Ars Technica'),
        ('hacker-news', 'Hacker News'),
        ('national-geographic', 'National Geographic'),
        ('new-scientist', 'New Scientist'),
        ('techcrunch', 'TechCrunch'),
        ('techradar', 'TechRadar'),
      ],
      'source': source,
    }
    return render(request, 'news/index.html', context)