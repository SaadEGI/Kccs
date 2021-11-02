import nest_asyncio
import twint
import csv

nest_asyncio.apply()

with open(r"ListofKeywords.txt") as f:
    lines = f.read().splitlines()
for a in lines:
    c = twint.Config()
    c.Search = a
    c.Lang = "eng"
    c.Min_likes = 10
    c.Limit = 1000
    c.Filter_retweets = True
    c.Custom["tweet"] = ["tweet", "username", "date", "likes_count"]
    print("yes")

    c.Output = "output.csv"
    c.Store_csv = True

    twint.run.Search(c)