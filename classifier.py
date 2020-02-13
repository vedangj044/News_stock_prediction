from model import Sentiment
from sklearn.externals import joblib 
from nltk import classify
from nltk.tokenize import word_tokenize


f = joblib.load('model.pkl')

class Classify:
    """
    This class classify the given news as Positive or Negative
    """
    def __init__(self, news):
        news = word_tokenize(news)
        self.news_token = Sentiment().remove_noise(token_=news)

    def classify(self):
        result = f.classify(dict([token, True] for token in self.news_token))
        return result
