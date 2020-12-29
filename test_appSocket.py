import unittest
from fastapi.testclient import TestClient
from fastapi.websockets import WebSocket
from appWebSocket import app

class socketCases(unittest.TestCase):

    def test_emptyQuery(self):
        client = TestClient(app)
        with client.websocket_connect("/ws") as ws:
            ws.send_text("")
            data = ws.receive_json()
            assert 'Invalid query' in data['message']

    def test_invalidQuery(self):
        client = TestClient(app)
        with client.websocket_connect("/ws") as ws:
            ws.send_text("case;';';';';'eenadue'")
            data = ws.receive_json()
            assert 'Google' in data['message']

    def test_invalidTicker(self):
        client = TestClient(app)
        with client.websocket_connect("/ws") as ws:
            ws.send_text("google")
            data = ws.receive_json()
            assert 'brand' in data['message']

    def test_flow(self):
        self.client = TestClient(app)
        with self.client.websocket_connect("/ws") as ws:
            ws.send_text("tesla")
            data = ws.receive_json()

            assert 'predictedPrice' in data
            assert 'graph' in data
            assert 'summary' in data

            assert data['predictedPrice']['1'] is not None
            assert data['predictedPrice']['7'] is not None
            assert data['predictedPrice']['15'] is not None
            assert data['predictedPrice']['30'] is not None
            assert len(data['graph']) > 0
            assert data['summary'] is not None
