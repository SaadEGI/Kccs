# This crawler is made to crawl a list of subreddits available @ giveSomeUrl
import requests
import json
import time

BASEURL='https://www.reddit.com'


subredditsList = []
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
        response = response.text
        index = 0
        for child in json.loads(response).get('data').get('children'):
            print(index)
            finalList[subreddit][str(index)] = json.loads(requests.get(f"{BASEURL}{child.get('data').get('permalink')}/.json", headers=noAuthHeaders).text)
            index = index + 1
    else: 
        errors +=1
        errorList.append(subreddit)

if(not os.path.exists('./CrawledData/')):
    os.mkdir('./CrawledData')
with open('./CrawledData'+f'{time.strftime("%Y%m%d-%H%M%S")}'+'.json', "w") as fp:
    json.dump(finalList, fp, indent = 4) 

print('errors: '+ str(errors)+'in:')
print(errorList)
