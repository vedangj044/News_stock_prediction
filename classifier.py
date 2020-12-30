from model import Sentiment
from nltk.tokenize import word_tokenize
import pickle


class Classify:

    def __init__(self, news):
        """ This class classify the given news as Positive or Negative """
        news = word_tokenize(str(news))
        self.news_token = Sentiment().remove_noise(token_=news)

    def classify(self):
        self.model_file = open('my_classifier.pickle', 'rb')
        self.pickle_file = pickle.load(self.model_file)

        self.m = self.pickle_file.prob_classify(dict([token, True] for token in self.news_token))

        self.model_file.close()
        return self.m.prob("Positive")
