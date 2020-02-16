import requests
from bs4 import BeautifulSoup
import yfinance as yf
import altair as alt

# a = input()
# query = "https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup={}&Country=all&Type=All".format(a)
# r = requests.get(query)
#
# soup_news = BeautifulSoup(r.content, "html.parser")
#
# for link in soup_news.find_all('td'):
#     print(link.text)
#     break

class stock_graph():

    def __init__(self, query):
        self.url = "https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup={}&Country=all&Type=All".format(query)
        self.get_ticker()

    def get_ticker(self):
        self.r = requests.get(self.url)
        self.stock = BeautifulSoup(self.r.content, "html.parser")

        for link in self.stock.find_all('td'):
            self.ticker = link.text
            break

    def get_history(self):
        print(self.ticker)
        self.tickerDF = yf.Ticker(self.ticker).history(period='1d', start='2019-1-1')

        return alt.Chart(self.tickerDF).mark_line(interpolate='step-after').encode(
            x='Date:T',
            y='High:Q'
        ).transform_filter(
            alt.datum.symbol == self.ticker
        ).to_dict()

    def current_price(self):
        self.current_url = "https://www.google.com/search?hl=en&source=hp&ei=VqpGXteVFIrYz7sPo-q4uAk&q={}+price&oq=FB+price&gs_l=psy-ab.3..0i70i250j0l9.1358.2923..3985...0.0..0.176.1079.0j8......0....1..gws-wiz.......0i131.8dqQ09EDw5E&ved=0ahUKEwjXmI-lnNHnAhUK7HMBHSM1DpcQ4dUDCAY&uact=5".format(self.ticker)

        self.r1 = request.get(self.current_url)
        self.price_page = BeautifulSoup(self.r1.content, "html.parser")
