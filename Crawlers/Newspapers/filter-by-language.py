import requests

nonEnglishWebsitesList = []

with open('WebsiteLists') as f:
    websiteList = [line.strip() for line in f]

for website in websiteList:
    try:
        request = requests.head(website)
    except Exception as exc:
        print(website)
        continue# try catch block: prints websites that *may* be down. Will be checked manually
    if 'Content-language' not in request.headers:
        nonEnglishWebsitesList.append(website + 'check here!')# website does not have a Content-language header, 
        # will be checked manually later. 
        # 'check here!' flag will be used to hint that a website will have to be manually checked
        continue
    if request.headers['Content-language'] != 'en': #
        nonEnglishWebsitesList.append(website)

with open('nonEnglishWebsitesList.txt', 'w') as f:
    for website in nonEnglishWebsitesList:
        f.write("%s\n" % website)
