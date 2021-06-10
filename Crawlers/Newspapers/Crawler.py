from newsfetch.google import google_search
from newsfetch.news import newspaper
import os
import time
import json
import sys
# TODO: change the program so that it takes keywords from a file, and in case its empty look for no keywords in specific

index = 0
websiteList = []
data = {}
file_path = sys.argv[1]

with open('Newspapers/WebsiteLists') as f:
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

filename = f'{time.strftime("%Y%m%d-%H%M%S")}_raw.json'

with open(rf'{file_path+"/Newspapers_raw.json"}', "w") as fp:
    json.dump(data, fp, indent = 4)