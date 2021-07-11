# This script filters websites for various reasons, including:
# 1. Website is not english
# 2. Server is too slow (takes more than 10 seconds to reply)
# 3. Server is down

# This script does not mutate the original list! instead it saves the result in another file by 
# the name of 'exclusivelyEnglishWebsitesList

from langdetect import detect
import requests

nonEnglishWebsitesList = []
with open('WebsiteLists') as f:
    websiteList = [line.strip() for line in f]

for website in websiteList:
    try:
        request = requests.get(website, timeout = 10)
    except Exception as exc:
        nonEnglishWebsitesList.append(website)
        nonEnglishWebsitesList.append('^ requestException')
        continue
    try:
        if request.status_code != 200:
            nonEnglishWebsitesList.append(website)
            nonEnglishWebsitesList.append('^ '+str(request.status_code))
            continue
        
    except Exception as err:
        nonEnglishWebsitesList.append(website)
        nonEnglishWebsitesList.append('^ status_codeException!')


    try:    
        if detect(request.text) != 'en':
            nonEnglishWebsitesList.append(website)
    except Exception as err:
        nonEnglishWebsitesList.append(website )
        nonEnglishWebsitesList.append('^ appendException!')



with open('nonEnglishWebsitesList.txt', 'w') as f:
    for website in nonEnglishWebsitesList:
        f.write("%s\n" % website)

exclusivelyEnglishWebsiteList = []

for website in websiteList: 
    if website not in nonEnglishWebsitesList: 
        EW.append(website)
with open('exclusivelyEnglishWebsitesList.txt', 'w') as f: 
    for website in exclusivelyEnglishWebsiteList: 
        f.write("%s\n" % website)