import requests
from bs4 import BeautifulSoup
import json
import datetime

class scraper():

    def __init__(self, keyword: str, limit=10, time_=1):
        self.time_=time_
        self.count=0
        self.url = "https://news.google.com/search?q={0}&hl=en-IN&gl=IN&ceid=IN:en"
        self.query = self.url.format("%".join(keyword.split()))
        self.request_news = requests.get(self.query)

        if self.request_news.status_code == 200:
            self.link_extract()
        else:
            print("Query not working !!!")

    def link_extract(self):
        self.soup_news = BeautifulSoup(self.request_news.content, "html.parser")

        self.results = []

        for link in self.soup_news.find_all('div', class_="NiLAwe"):
            a_tag = link.find_all('a')
            if a_tag:
                l = a_tag[0]['href']
                title = link.find('h3').text
                time_value = link.find('time')["datetime"]
                now = datetime.datetime.now()
                time = datetime.datetime.strptime(time_value, '%Y-%m-%dT%H:%M:%SZ')
                if self.count==10:
                    break
                if (now-time).days>self.time_:
                    continue
                item = {
                    "title": title,
                    "link": "https://news.google.com/"+l,
                    "time": time_value
                }
                self.results.append(item)
            self.count+=1

    def pretty_print(self):
        data = json.dumps(self.results)
        f = open("data.json", "w")
        f.write(data)
        f.close()

    def get_title(self):
        news = ''
        for i in self.results:
            news += ". " + i['title']
        return news


if __name__ == "__main__":
    sc = scraper("Tesla Stocks")
    sc.pretty_print()

