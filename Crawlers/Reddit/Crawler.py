# This crawler is made to crawl a list of subreddits available @ giveSomeUrl
import requests
import json
import time
import os
import sys

BASEURL='https://www.reddit.com'


finalList = {}
errorList = []
errors = 0

with open('SubredditList') as f:
    subredditsList = [line.strip() for line in f]

noAuthHeaders = {"User-Agent": "ViralOutbreakDetector/0.1 (by /u/KCCS_throwaway)"}

for subreddit in subredditsList:
    finalList[subreddit]={}
    response = requests.get(f"{BASEURL}{subreddit}/.json?&limit=1000&after30d", headers=noAuthHeaders)
    if(response.status_code == 200):
        index = 0
        for child in response.json()['data']['children']:
            finalList[subreddit][str(index)] = requests.get(f"{BASEURL}{child.get('data').get('permalink')}/.json", headers=noAuthHeaders).json()
            index = index + 1
    else: 
        errors +=1
        errorList.append(subreddit)

finalList['errors'] = {
    'faulty subreddits': errorList,
    'numErrors': errors
}
if(not os.path.exists('./CrawledData/')):
    os.mkdir('./CrawledData')

filename = f'{time.strftime("%Y%m%d-%H%M%S")}_raw.json'

with open(f'./CrawledData/{filename}', "w") as fp:
    json.dump(finalList, fp, indent = 4)

print(f'{filename}')
sys.exit(0)

