import unittest
from predictor import predict1
import pandas as pd
from model import Sentiment
from nltk import NaiveBayesClassifier
from extractTicker import stock_graph
from news_scraper import scraper
from AltException import InvalidQuery, InvalidTicker

class newsScraperTestcase(unittest.TestCase):

    def setUp(self):
        self.scr = scraper("Tesla")

    def test_news_scraper(self):
        self.assertTrue(len(self.scr.results)>0)

    def test_news_count(self):
        self.assertTrue(self.scr.count>0)

    def test_get_title(self):
        self.assertIsInstance(self.scr.get_title(), str)

    def test_empty_scaper(self):
        self.assertRaises(AssertionError, lambda: scraper(""))

    def test_invalid_scraper(self):
        self.assertRaises(InvalidQuery, lambda: scraper("icneidisneafebf"))

class predictorTestCase(unittest.TestCase):

    def setUp(self):
        self.pred = predict1("Tesla")

    def test_predictor(self):
        self.assertTrue(self.pred.final_pred)

    def test_empty_predictor(self):
        self.assertRaises(AssertionError, lambda: predict1(""))

    def test_invalid_predictor(self):
        self.assertRaises(InvalidQuery, lambda: predict1("iaenflaisuef"))

class modelTestCase(unittest.TestCase):

    def test_model_train(self):
        self.model = Sentiment().train_data()
        self.assertIsInstance(self.model, NaiveBayesClassifier)

class extractTicketTestCase(unittest.TestCase):

    def setUp(self):
        self.sg = stock_graph("Tesla", [0.08733508525853388, 0.41467300402115265, 0.8421720201029591, 2.1635118971243883])

    def test_ticker(self):
        self.assertEqual(self.sg.ticker, "TSLA")

    def test_current_value(self):
        self.assertTrue(self.sg.current_price_value)

    def test_graph(self):
        self.assertIsInstance(self.sg.graph(), dict)

    def test_empty_graph(self):
        self.assertRaises(AssertionError, lambda: stock_graph("", []))

    def test_invalid_graph(self):
        self.assertRaises(InvalidTicker, lambda: stock_graph("google",
        [0.08733508525853388,
        0.41467300402115265,
        0.8421720201029591,
        2.1635118971243883]))


if __name__ == "__main__":
    unittest.main() # pragma: no cover
