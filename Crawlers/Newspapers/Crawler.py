from newsfetch.google import google_search
from newsfetch.news import newspaper
import os
import time
import json
import sys

index = 0
data = {}
file_path = sys.argv[1]

with open('Newspapers/WebsiteLists') as f:
    websiteList = [line.strip() for line in f]
with open('Newspapers/Keywords') as f:
    KeywordList = [line.strip() for line in f]

for website in websiteList:
    for keyword in KeywordList:
        query = google_search(keyword, website, query_params='w', num_pages=2)
        if(query is True):
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
        else:
            print("Google has not found any result in {}".format(website))

filename = f'{time.strftime("%Y%m%d-%H%M%S")}_raw.json'

with open(rf'{file_path+"/Newspapers_raw.json"}', "w") as fp:
    json.dump(data, fp, indent = 4)