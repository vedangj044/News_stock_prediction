import unittest
from predictor import predict1
import pandas as pd
from extractTicker import stock_graph
from news_scraper import scraper

class newsScraperTestcase(unittest.TestCase):

    def test_news_scraper(self):
        self.scr = scraper("Tesla")
        self.assertTrue(len(self.scr.results)>0)
        self.assertTrue(self.scr.count>0)
        self.assertIsInstance(self.scr.get_title(), str)

class predictorTestCase(unittest.TestCase):

    def test_predictor(self):
        self.pre = predict1("Tesla")
        self.assertTrue(self.pre.final_pred)

class extractTicketTestCase(unittest.TestCase):

    def test_extractor(self):
        self.sg = stock_graph("Tesla", [0.08733508525853388, 0.41467300402115265, 0.8421720201029591, 2.1635118971243883])
        self.assertEqual(self.sg.ticker, "TSLA")
        self.assertTrue(self.sg.current_price_value)
        self.assertIsInstance(self.sg.graph(), dict)

if __name__ == "__main__":
    unittest.main()
