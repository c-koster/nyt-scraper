import requests
import os
import json
# scrape stuff

from dotenv import load_dotenv

load_dotenv() # fetch env variables from my .env file
api_key = os.environ.get("NYT_API")
api_secret = os.environ.get("NYT_SECRET")
monkey_secret = os.environ.get("MONKEY_KEY")


nyt_url = "https://api.nytimes.com/svc/news/v3/content/all/climate.json?api-key=" + api_key
monkey_url = "https://api.monkeylearn.com/v3/classifiers/cl_pi3C7JiL/classify/"

def search_envs():
    """
    Get me a list of page objects from the climate tab

    """
    news_results = requests.get(nyt_url)
    t = json.loads(news_results.content)
    #print(t)
    return t["results"]

def get_happy_articles(cutoff=.8):
    """
    gets a list of recent NYT articles and runs them through a sentiment analysis engine. If
    """
    articles = search_envs()
    abstracts = []
    for i in articles:
        d = i["abstract"]
        abstracts.append(d)

    data = {"data":abstracts}
    head = {"Authorization":"Token "+ monkey_secret,"Content-Type":"application/json"}
    sentiment_results = requests.post(monkey_url,headers=head,data=json.dumps(data))
    t = json.loads(sentiment_results.content)
    for i in range(len(t)):
        tag = t[i]["classifications"][0]["tag_name"]
        if (tag != "Negative"):
            a = articles[i]
            print("-"*20)
            print(a["title"] + "--" + tag)
            print(a["url"])







if __name__ == '__main__':
    get_happy_articles()
