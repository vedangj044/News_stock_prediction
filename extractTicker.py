import requests
from bs4 import BeautifulSoup
import yfinance as yf
import altair as alt
import pandas as pd
from datetime import timedelta, datetime
import urllib.request
import json
import dateutil.relativedelta
import os
from AltException import InvalidTicker


class stock_graph():

    def __init__(self, query, regression_output):
        """ Summary of the class here

        query: the name of the brand
        regression_output: list of 4 elements having the predicted change in
        the price values
        """
        self.regression_output = regression_output
        self.url = "https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup={}&Country=all&Type=All".format(query)
        assert query != ""
        self.get_ticker()
        self.get_history()
        self.current_price()

    def get_ticker(self):
        """
        User provides the company name, not ticker
        Extract the ticker name, from marketwatch.com
        """

        self.r = requests.get(self.url)
        self.stock = BeautifulSoup(self.r.content, "html.parser")

        for link in self.stock.find_all('td'):
            self.ticker = link.text
            break

        if not hasattr(self, 'ticker'): raise InvalidTicker


    def get_history(self):
        """ Consuming yfinance api to get stock price history """

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

    def current_price(self):
        """ Get the current stock price from financialmodelingprep.com """

        key = "aeb9ccb3e78f3a9864269a04447db4e8"
        # key = os.environ["key"]
        self.url_current = "https://financialmodelingprep.com/api/v3/quote/{0}?apikey={1}".format(self.ticker, key)
        req = urllib.request.Request(self.url_current)
        with urllib.request.urlopen(req) as response:
            self.response_current = response
            data = json.loads(self.response_current.read().decode("utf-8"))
            if len(data) == 0: raise InvalidTicker
            self.current_price_value = data[0]['price']
            self.predict_price()

    def predict_price(self):
        """ Added the predicated values from the model to the stock-price vs time data. """
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

    def graph(self):
        """ Using Altair to generate graph """

        base = alt.Chart(self.final_dataset).mark_line().encode(
            x='date:T',
            y='price:Q',
            color='color:O'
        ).configure_projection(
            scale=10
        ).interactive()
        return base.to_dict()

    def graphSocket(self):
        """ Return dictionary to generate graph on the client side """

        self.final_dataset.reset_index(inplace=True)
        return json.dumps(list(self.final_dataset.to_dict(orient="Index").values()), default=str)

# s = stock_graph('tesla', [5.093, 0.524, 1.082, 2.355])
# print(s.ticker)
# print(s.graphSocket())
