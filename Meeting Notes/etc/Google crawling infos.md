## Best Practices On How To Scrape The Web Without Getting Blocked
### 1. Use IP Rotation
### 2. Set A Referrer (good idea for reddit and twitter)
### 3. Add In Random Sleep Delays And Actions
### 4. Rotate User Agents and corresponding HTTP Request Headers between requests
[check this link for more details](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/)

### 5. Some experience from scarping google
- What exactly do you want to scrape? I'm scraping approx 40k Google News results at the moment and added a SleepTimer range from 30-180 secs after every request. Scraper is running for approx 6 hrs at the moment.

I'm pretty new to scraping/ python but managed to realise a project I've had in mind. To prevent a blocking of my local IP i'm using a VPN for scraping which seems to work fine so far.

You can display max 100 search results per Google page. If you add "&num=100" to your search string, each request will put 100 search results (div class="g") into your soup.

If you're adding "&start=" to your search string you can "skip" results, i.e. the first 100.

So what I'm doing is

    search for max results ("&num=100")

    count number of pages (table class="AaVjTc" , class="FL")

    Iterate over the number of pages while changing the "&start=" parameter in my search string

    time.sleep after every request
Rotating user-agent won't help if you keep the same IP address for every request, you need rotating proxies as well.

- Make no more than one request every 3-10 seconds (vary the time). Google thinks you're typing. I haven't tried a thousand items (!), but that's worked for me.

- If you want a free search API, duckduckgo can work reasonably well. Google is ferocious with blocking automated scrapers.
### 6. different infos
- Google Custom Search gives you 100 queries per day for free. · After that you pay $5 per 1000 queries.

- If you want a free search API, duckduckgo can work reasonably well. Google is ferocious with blocking automated scrapers.
## Fazit: Google will definitly ban you if you abuse them
### my suggested solution: use a VPN


