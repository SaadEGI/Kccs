from newsfetch.google import google_search
from newsfetch.news import newspaper
import os
import time
import json
import sys

index = 0
data = {}
file_path = sys.argv[1]
filename = f'{time.strftime("%Y%m%d-%H%M%S")}_raw.json'
proxy_list = []


with open('Newspapers/ProxyList') as f:
    proxy_list = [line.strip() for line in f]


with open('Newspapers/WebsiteLists') as f:
    websiteList = [line.strip() for line in f]
with open('Newspapers/Keywords') as f:
    KeywordList = [line.strip() for line in f]

for website in websiteList:
    data[website] = []
    for keyword in KeywordList:
        proxy = None
        try:
            proxy = proxy_list.pop()
        except Exception as err:
            print(err)
        if(proxy is not None):
            query = google_search(keyword, website, query_params='m', num_pages=1, proxy = proxy)
        else:
            query = google_search(keyword, website, query_params='m', num_pages=1)
        if(hasattr(query, 'urls')):
            print(website)
            for url in query.urls:
                article = newspaper(url)
                data[website][index] = {
                    'Title': article.headline,
                    'Website': article.source_domain,
                    'Description': article.description,
                    'Main Text': article.article,
                    'URL': article.uri
                }
                index = index + 1
                with open(rf'{file_path+"/Newspapers_raw.json"}', "w") as fp:
                    json.dump(data, fp, indent = 4)
        else:
            print("ERROR:/Google has not found any result in {}".format(website))