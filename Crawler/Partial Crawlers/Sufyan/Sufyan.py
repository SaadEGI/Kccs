# This crawler is made to crawl a list of subreddits available @ giveSomeUrl
import urllib.request
import urllib.parse
import requests
import json
import time

BASEURL='https://www.reddit.com'

# TODO: replace appends with list comprehension, use less for loops

subredditsList = []
crawledSubredditData = []
List = []
# finalList = pd.DataFrame()
finalList = {}
errors = 0

with open('SubredditList') as f:
    for line in f:
        subredditsList.append(line.strip())



# Start Authentication
# app_id = RaXEyN-z0yuWdw
# app_secret = y_6SexbQwH4ym8533LxB420gSxGu7Q
# client_auth = requests.auth.HTTPBasicAuth('RaXEyN-z0yuWdw', 'y_6SexbQwH4ym8533LxB420gSxGu7Q')
# # reddit_username = KCCS_throwaway
# # reddit_password = bqDv9fn4mRauQiZ
# post_data = {"grant_type": "password", "username": "KCCS_throwaway", "password": "bqDv9fn4mRauQiZ"}
# headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}

# response = json.loads(requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers).text)


# RedditAuthToken = 'Bearer '+response["access_token"]
# # print('response: \n'+RedditAuthToken)
# authHeaders = {"Authorization": RedditAuthToken, "User-Agent": "ViralOutbreakDetector/0.1 (by /u/KCCS_throwaway)"}
noAuthHeaders = {"User-Agent": "ViralOutbreakDetector/0.1 (by /u/KCCS_throwaway)"}
# End Authentication
# >>> print(json.loads(requests.get('https://www.reddit.com/r/Mewing/.json?&limit=1000&after30d', headers={"User-Agent": "ViralOutbreakDetector/0.1 (by /u/KCCS_throwaway)"}).text)['data'])



# reddit@reddit-VirtualBox:~$ curl -H "Authorization: bearer J1qK1c18UUGJFAzz9xnH56584l4" -A "ChangeMeClient/0.1 by YourUsername" https://oauth.reddit.com/api/v1/me

# https://www.git .com/dev/api/#GET_{sort}
# + https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example
#1. Get a list of all posts of the last month throught the two above pages

# https://www.reddit.com/r/{{}}/.json?&limit=1000&after30d
# printrequests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
for subreddit in subredditsList:
    finalList[subreddit]={}
    # for subList in requests.get(f"{BASEURL}{subreddit}/.json?&limit=1000&after30d", headers=noAuthHeaders).text:
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
        # List.append(child)
        # List.append(requests.get(f"{BASEURL}{subreddit}/{child.get('permalink')}/.json"))
# finalList.to_json('crawledData'+f'{time.strftime("%Y%m%d-%H%M%S")}'+'.json', orient = 'table', compression = 'infer', index = 'true') #otherwise orient can be specified as split, but idk
with open('crawledData'+f'{time.strftime("%Y%m%d-%H%M%S")}'+'.json', "w") as fp:
    json.dump(finalList, fp, indent = 4) 

print('errors: '+ str(errors))

# with open('finalList.json', 'w') as jsonfile:
#     json.dump(data, jsonfile)



# finalList .append()

# 2. crawl the posts individually by appending the .json to its end. this will return two objects, the first one at index 0 
# includes the post, the second object at index 1 includes the comments


# 3. save posts in a folder called scraped data or smth in json format
# 3.1 maybe use pandas and dataframes for dealing with the data 

# TODO:save .json files in a folder, format the files when saving so that they are more readable and are 
# all saved on one single file 

# TODO; add some code so you can know of which subreddit or post the error is caused