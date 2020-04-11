import requests
from bs4 import BeautifulSoup
import yfinance as yf
import altair as alt
import pandas as pd
from datetime import date, timedelta
from urllib.request import urlopen
import json


class stock_graph():

    def __init__(self, query, regression_output):
        self.regression_output = regression_output
        self.url = "https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup={}&Country=all&Type=All".format(query)
        self.get_ticker()
        self.current_price()
        self.get_history()

    def get_ticker(self):
        self.r = requests.get(self.url)
        self.stock = BeautifulSoup(self.r.content, "html.parser")

        for link in self.stock.find_all('td'):
            self.ticker = link.text
            break

    def get_history(self):
        self.tickerDF = yf.Ticker(self.ticker).history(period='1d', start='2020-2-26')
        self.tickerDF_converted = {'date': [],
                                   'price': [],
                                   'color': []}

        data = pd.DataFrame(self.tickerDF, columns=['Open'])
        for i in data.iterrows():
            self.tickerDF_converted['date'].append(i[0])
            self.tickerDF_converted['price'].append(i[1][0])
            self.tickerDF_converted['color'].append('a')

        self.tickerDF_converted['date'].append(date.today())
        self.tickerDF_converted['price'].append(self.current_price_value)
        self.tickerDF_converted['color'].append('a')
        self.tickerDF_converted = pd.DataFrame(self.tickerDF_converted)

    def current_price(self):
        self.url_current = "https://financialmodelingprep.com/api/v3/quote/{}".format(self.ticker)
        self.response_current = urlopen(self.url_current)
        data = self.response_current.read().decode("utf-8")
        self.current_price_value = json.loads(data)[0]['price']
        self.predict_price()

    def predict_price(self):
        self.predict_price_value = {'date': [pd.to_datetime('today'),
                                            pd.to_datetime('today')+timedelta(days=1),
                                            pd.to_datetime('today')+timedelta(days=7),
                                            pd.to_datetime('today')+timedelta(days=15),
                                            pd.to_datetime('today')+timedelta(days=30),
                                            ],
                                    'price': [self.current_price_value],
                                    'color': ['b',"b","b","b","b"]}

        for i in self.regression_output:
            temp_data = self.current_price_value+(self.current_price_value*i)/100
            self.predict_price_value['price'].append(temp_data)

        self.predict_price_value = pd.DataFrame(self.predict_price_value)

    def graph(self):
        self.final_dataset = self.predict_price_value.append(self.tickerDF_converted)
        base = alt.Chart(self.final_dataset).mark_line().encode(
            x='date:T',
            y='price:Q',
            color='color:O'
        ).configure_projection(
            scale=10
        )
        return base.to_dict()

# s = stock_graph('infosys', [5.093, 0.524, 1.082, 2.355])
# print(s.ticker)
# print(s.graph())
