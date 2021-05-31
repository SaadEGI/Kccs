from newsfetch.google import google_search
from newsfetch.news import newspaper
import os
import time
import json

index = 0
websiteList = []
data = {}

with open('WebsiteLists') as f:
        websiteList = [line.strip() for line in f]

for website in websiteList:
    query = google_search('women', website, query_params='w', num_pages=2)
    for url in query.urls:
        article = newspaper(url)
        data[index] = {
            'Title': article.headline,
            'Website': article.source_domain,
            'Description': article.description,
            'Main Text': article.article,
            'URL': article.uri
        }
        index = index + 1


if(not os.path.exists('./CrawledData/')):
    os.mkdir('./CrawledData')

filename = f'{time.strftime("%Y%m%d-%H%M%S")}_raw.json'

with open(f'./CrawledData/{filename}', "w") as fp:
    json.dump(data, fp, indent = 4)


# https://www.google.com/search?q={{seach query}}&tbs=qdr:m
<<<<<<< HEAD

# https://stackoverflow.com/questions/19943022/import-a-python-library-from-github
=======
>>>>>>> f3a735979ea13eb3155b837dbf3b8d5ed0e6b532
