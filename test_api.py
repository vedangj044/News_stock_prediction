from app import app
import unittest
import flask
from flask_sqlalchemy import SQLAlchemy
from app import db, app
import json

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

    def test_endpoints_fake_ticker(self):
        self.assertEqual(self.app.get("/news?query=desdaey';';'aefaeuf").status_code, 404)
        self.assertEqual(self.app.get("/stock-graph?query=desdaey';';'aefaeuf").status_code, 404)
        self.assertEqual(self.app.get("/get-summary?query=desdaey';';'aefaeuf").status_code, 404)

    def checkResponse(self, resp):
        assert len(resp["predict"]) == 4
        assert resp["predict"]["1"] is not None
        assert resp["predict"]["7"] is not None
        assert resp["predict"]["15"] is not None
        assert resp["predict"]["30"] is not None


    def test_response_object(self):
        try:
            self.checkResponse(json.loads(self.app.get("/news?query=Tesla").data))
        except Exception as e: # pragma: no cover
            self.fail(msg="Response format is invalid") # pragma: no cover

    def test_invalid_ticker(self):
        self.assertEqual(self.app.get("/news?query=google").status_code, 200)
        self.assertEqual(self.app.get("/stock-graph?query=google").status_code, 404)
