from classifier import Classify
from news_scraper import scraper

class predict1():

    def __init__(self, keyword, scraperResults=None):
        """Calls the scraper and returns the sentiment score of the news headlines."""
        self.score = 0
        self.articles = 0
        assert keyword != ""
        self.keyword = keyword
        self.sc = scraperResults
        self.predictor()

    def predictor(self):
        if self.sc == None:
            self.sc = scraper(self.keyword).results
        self.articles = len(self.sc)

        for i in self.sc:
            value = Classify(i["title"]).classify()
            self.score+=value

        self.final_pred = self.score/self.articles
