from model import Sentiment
from nltk import classify
from nltk.tokenize import word_tokenize
import pickle
from nltk.probability import UniformProbDist as U

model_file = open('my_classifier.pickle', 'rb')
f = pickle.load(model_file)

class Classify:
    """
    This class classify the given news as Positive or Negative
    """
    def __init__(self, news):
        news = word_tokenize(str(news))
        self.news_token = Sentiment().remove_noise(token_=news)

    def classify(self):
        m = f.prob_classify(dict([token, True] for token in self.news_token))
        return m.prob("Positive")
