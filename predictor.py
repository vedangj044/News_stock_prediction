from classifier import Classify
from news_scraper import scraper
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import json

class predict1():

    def __init__(self, keyword):
        self.score = 0
        self.articles = 0
        self.keyword = keyword
        self.predictor()

    def predictor(self):
        sc = scraper(self.keyword).results
        self.articles = len(sc)

        for i in sc:
            value = Classify(i["title"]).classify()
            self.score+=value

        self.final_pred = self.score/self.articles

    # for test purposes
    # def resp(self):
    #     return json.dumps({"score": self.final_pred, "articles": self.articles})
