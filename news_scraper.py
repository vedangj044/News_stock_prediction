import requests
from bs4 import BeautifulSoup
import json

class scraper():

    def __init__(self, keyword: str, limit=10):
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
                item = {
                    "title": title,
                    "link": "https://news.google.com/"+l
                }
                self.results.append(item)

    def pretty_print(self):
        data = json.dumps(self.results)
        f = open("data.json", "w")
        f.write(data)
        f.close()


if __name__ == "__main__":
    sc = scraper("Tesla Stocks")
    sc.pretty_print()
