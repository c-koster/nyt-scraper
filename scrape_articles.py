import requests
import os
import json
# scrape stuff

from sentiment import *
from dotenv import load_dotenv

load_dotenv() # fetch env variables from my .env file
api_key = os.environ.get("NYT_API")
api_secret = os.environ.get("NYT_SECRET")


url = "https://api.nytimes.com/svc/news/v3/content/all/climate.json?api-key=" + api_key

def search_envs():
    """
    Get me a list of page objects from the climate tab

    """
    news_results = requests.get(url)
    t = json.loads(news_results.content)
    #print(t)
    return t["results"]

def get_happy_articles(cutoff=.8):
    """
    gets a list of recent NYT articles and runs them through a sentiment analysis engine. If
    """
    articles = search_envs()
    for i in articles:
        print(i["abstract"] +"\n------")


if __name__ == '__main__':
    get_happy_articles()
