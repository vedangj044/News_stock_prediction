import requests
from bs4 import BeautifulSoup

class scraper():

    def __init__(keyword: str, limit=10: int):
        self.url = f"https://news.google.com/search?q={}&hl=en-IN&gl=IN&ceid=IN:en"
        self.query = self.url.format("%".join(keyword.split()))
        self.request_news = requests.get(self.query)

        if self.request_news.status_code == 200:
            self.link_extract()
        else:
            print("Query not working !!!")

    def link_extract():
        self.soup_news = BeautifulSoup(self.request_news.content, "html.parser")

        self.results = []

        for link in self.soup_news.find_all('div', class_='r'):
            a_tag = g.find_all('a')
            if a_tag:
                l = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                self.results.append(item)

        self.pretty_print()

    def pretty_print():
        json.dumps(self.results)


if __name__ == "__main__":
    sc = scraper()
