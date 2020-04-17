from app import app
import unittest
import flask
from flask_sqlalchemy import SQLAlchemy
from app import db, app

class endpointsCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite3'
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()


    def tearDown(self):
        db.drop_all()

    def test_empty_query(self):
        self.assertEqual(self.app.get("/news").status_code, 404)
        self.assertEqual(self.app.get("/stock-graph").status_code, 404)
        self.assertEqual(self.app.get("/get-summary").status_code, 404)

        self.assertEqual(self.app.get("/stock-graph?query=tata").status_code,
                                      404)


    def test_endpoints_status_code(self):
        self.assertEqual(self.app.get("/news?query=tesla").status_code, 200)
        self.assertEqual(self.app.get("/stock-graph?query=tesla").status_code, 200)
        self.assertEqual(self.app.get("/get-summary?query=tesla").status_code, 200)

        self.assertEqual(self.app.get("/news?query=tesla").status_code, 200)
