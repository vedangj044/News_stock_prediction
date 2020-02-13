from classifier import Classify
from news_scraper import scraper
import json

class predict():

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
            if value == "Positive":
                self.score+=1

        self.final_pred = self.score/self.articles
        

    def resp(self):
        
        return json.dumps({"score": self.final_pred, "articles": self.articles})
