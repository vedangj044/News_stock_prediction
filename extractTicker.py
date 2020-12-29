import requests
from bs4 import BeautifulSoup
import yfinance as yf
import altair as alt
import pandas as pd
from datetime import date, timedelta, datetime
from urllib.request import urlopen
import json
import dateutil.relativedelta
import os
from AltException import InvalidTicker


class stock_graph():

    """
    Plotting the graph of stock price vs time, including future prediction
    """
    def __init__(self, query, regression_output):
        self.regression_output = regression_output
        self.url = "https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup={}&Country=all&Type=All".format(query)
        assert query != ""
        self.get_ticker()
        self.get_history()
        self.current_price()

    """
    User provides the company name, not ticker
    Extract the ticker name, from marketwatch.com
    """
    def get_ticker(self):
        self.r = requests.get(self.url)
        self.stock = BeautifulSoup(self.r.content, "html.parser")

        for link in self.stock.find_all('td'):
            self.ticker = link.text
            break

        if not hasattr(self, 'ticker'): raise InvalidTicker

    """
    Consuming yfinance api to get stock price history
    """
    def get_history(self):
        self.one_mon = datetime.now() + dateutil.relativedelta.relativedelta(months=-1)
        self.one_mon = str(self.one_mon)[0:10]
        self.tickerDF = yf.Ticker(self.ticker).history(period='1d', start=self.one_mon)
        self.tickerDF_converted = {'date': [],
                                   'price': [],
                                   'color': []}

        data = pd.DataFrame(self.tickerDF, columns=['Open'])
        for i in data.iterrows():
            self.tickerDF_converted['date'].append(i[0])
            self.tickerDF_converted['price'].append(i[1][0])
            self.tickerDF_converted['color'].append('a')

        self.tickerDF_converted = pd.DataFrame(self.tickerDF_converted)

    """
    Get the current stock price from financialmodelingprep.com
    """
    def current_price(self):
        key = os.environ["key"]
        self.url_current = "https://financialmodelingprep.com/api/v3/quote/{0}?apikey={1}".format(self.ticker, key)
        self.response_current = urlopen(self.url_current)
        data = json.loads(self.response_current.read().decode("utf-8"))
        if len(data) == 0: raise InvalidTicker
        self.current_price_value = data[0]['price']
        self.predict_price()

    """
    Added the predicated values from the model to the stock-price vs time data.
    """
    def predict_price(self):
        self.predict_price_value = {'date': [pd.to_datetime('today').date(),
                                            (pd.to_datetime('today')+timedelta(days=1)).date(),
                                            (pd.to_datetime('today')+timedelta(days=7)).date(),
                                            (pd.to_datetime('today')+timedelta(days=15)).date(),
                                            pd.to_datetime('today')+timedelta(days=30),
                                            ],
                                    'price': [self.current_price_value],
                                    'color': ['b',"b","b","b", "b"]}

        for i in self.regression_output:
            temp_data = self.current_price_value+(self.current_price_value*i)/100
            self.predict_price_value['price'].append(temp_data)

        self.predict_price_value = pd.DataFrame(self.predict_price_value)
        self.final_dataset = self.tickerDF_converted.append(self.predict_price_value)

    """
    Using Altair to generate graph
    """
    def graph(self):
        base = alt.Chart(self.final_dataset).mark_line().encode(
            x='date:T',
            y='price:Q',
            color='color:O'
        ).configure_projection(
            scale=10
        ).interactive()
        return base.to_dict()

# s = stock_graph('google', [5.093, 0.524, 1.082, 2.355])
# print(s.ticker)
# s.graph()
