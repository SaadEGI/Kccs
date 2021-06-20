from newsfetch.google import google_search
from newsfetch.news import newspaper
import os
import time
import json
import sys

index = 0
data = {}
filename = f'Crawlers/{time.strftime("%Y%m%d-%H%M%S")}_raw.json'


with open('Crawlers/Newspapers/WebsiteLists') as f:
    websiteList = [line.strip() for line in f]
with open('Crawlers/Newspapers/Keywords') as f:
    KeywordList = [line.strip() for line in f]

for website in websiteList:
    data[website] = {}
    for keyword in KeywordList:
        query = google_search(keyword, website, query_params='m', num_pages=1)
        if(hasattr(query, 'urls')):
            print(website)
            for url in query.urls:
                data[website][index] = url
                index = index + 1
                with open(rf'{filename+"/Newspapers_raw.json"}', "w") as fp:
                    json.dump(data, fp, indent = 4)
        else:
            print("ERROR:/Google has not found any result in {}".format(website))