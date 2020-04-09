from app import app
import unittest
import flask

class endpointsCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_empty_query(self):
        result = self.app.post("/news")
        self.assertEqual(result.status_code, 200)

    def test_endpoints_status_code(self):
        result = self.app.post("/news", data={"query": "tesla"})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(self.app.get("/stock-graph").status_code, 200)
        summary = self.app.get("/get-summary", follow_redirects=True)
        self.assertEqual(summary.status_code, 200)
