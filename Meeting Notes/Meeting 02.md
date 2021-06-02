# KCCS Meeting 2


Session               | 08.05.2021
----------------------|-
Protocol organizer    | Sufyan Dahalan
Present members       | Saad Bendou, Sufyan Dahalan, Mohamad Almortada
Absent members        | -
Begin                 | 17:00
End                   | 19:25

Opened Issues
---
- Data
    1. Data sources:
        - newspapers: Using intersection of Alexa most visited websites and the most popular (minimum of 100) newspapers in the country or region for which the prediction is gonna be made 
        - twitter: to be secondary, not to be necessarily relied upon
        - blog posts: saad suggests following known blogs
        - reddit: follow subreddits of countries
        - optional: governmental institues, official reports and statements
    2. Data types: newspaper articles, twitter tweets, blog posts, reddit posts
    3. Topics: outbreaks, viral infections (in unusual amounts), symptoms, multiples of people with same infections or symptoms, 
    4. Recehncy of data: last month - last day
    5. Retrieved features: author, date, title, source, organization, text (body)
    6. Derived features: number of words, keywords, political inclination, sentiment, semantic analysis
    7. Data organisation:  json files (one containing the original scrap,one containing its cleaned copy, and one containing derived features), dataframes compatible, to be saved in an organised folder structure (<=> aka not in a DB!)
     
 

Agreed upon Tasks
---
- Everybody will read [the](https://www.aclweb.org/anthology/2020.nlpcovid19-acl.1/) [paper](https://www.semanticscholar.org/paper/CORD-19%3A-The-COVID-19-Open-Research-Dataset-Wang-Lo/4a10dffca6dcce9c570cb75aa4d76522c34a2fd4) and practice news-please and [read](https://github.com/fhamborg/news-please/wiki/pipeline) [its](https://github.com/fhamborg/news-please/wiki/configuration) [docs](https://github.com/fhamborg/news-please)

- Saad will collect blogs and newspapers to be scraped, sufyan will collect subreddits to be scraped, mohamad will collect a list of most followed journalists on twitter categorized by country
---
Meeting ended on 08.05.2021 at 19:25. Next meeting will be on the 11.05.2021 at 18:00 via Zoom.
