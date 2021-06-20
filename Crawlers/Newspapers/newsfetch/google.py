from newsfetch.helpers import (get_chrome_web_driver, get_web_driver_options,
                               set_automation_as_head_less,
                               set_browser_as_incognito,
                               set_ignore_certificate_error, set_proxy)
from newsfetch.utils import (BeautifulSoup, Options, UserAgent,
                             chromedriver_binary, get, re, sys, time,
                             webdriver)

class google_search:

    def __init__(self, keyword, newspaper_url, query_params=None, num_pages = 1, proxy = None):

        self.keyword = keyword
        self.newspaper_url = newspaper_url

        random_headers = {'User-Agent': UserAgent().random,
                          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
        self.search_term = '"{}" site:{}'.format(self.keyword, self.newspaper_url)



        if(query_params == 'd'):
            self.query_params = '&tbs=qdr:d'
        elif(query_params == 'w'):
            self.query_params = '&tbs=qdr:w'
        elif(query_params == 'm'):
            self.query_params = '&tbs=qdr:m'
        elif(query_params == 'y'):
            self.query_params = '&tbs=qdr:y'
        else:
            self.query_params = ''


        self.num_pages = num_pages


        url = "https://www.google.com/search?q={}{}".format('+'.join(self.search_term.split()), self.query_params)

        options = get_web_driver_options()
        # set_automation_as_head_less(options)
        set_ignore_certificate_error(options)
        # set_browser_as_incognito(options)
        if(proxy is not None):
            set_proxy(options, proxy)

        
        driver = get_chrome_web_driver(options)
        driver.get(url)
        
        url_list = []

        try:
            if len(driver.find_elements_by_xpath('//div[@id="result-stats"]')) != 0:
                
                results = driver.find_elements_by_xpath(
                    '//div[@id="result-stats"]')[0].get_attribute('innerHTML')

                results = results[:results.find('Ergebnisse')]
                max_pages = round(
                    int(int(''.join(i for i in results if i.isdigit()))) / 10)

            if max_pages < self.num_pages:
                self.num_pages = max_pages
                print('Google returned only {} pages, I may have to cut down on result'.format(max_pages, max_pages))

            if max_pages != 0:

                index = 0

                while True:
                    try:
                        index += 1
                        links = driver.find_elements_by_xpath(
                            '//div[@class="yuRUbf"]/a')
                        linky = [link.get_attribute('href') for link in links]
                        url_list.extend(linky)
                        try:
                            driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]').click()
                        except Exception as err:
                            if index < self.num_pages:
                                driver.get('{}&start={}'.format(url, index*10))
                                continue
                            else:
                                break
                        time.sleep(2)
                        sys.stdout.write('\r No. of pages parsed : %s\r' % (str(index)))
                        sys.stdout.flush()
                    except Exception as err:
                        if (index+1) % 10 == 0 and index < self.num_pages:
                            driver.get('{}&start={}'.format(url, index+1))
                        else:
                            continue

                driver.quit()
            else:
                print(
                    'Your search - %s - did not match any documents.' % str(self.search_term))
            url_list = list(dict.fromkeys(url_list))
            url_list = [url for url in url_list if '.pdf' not in url]
            self.urls = [url for url in url_list if '.xml' not in url]

        except Exception as err:
            self = False