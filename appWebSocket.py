from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
from app_helper import pre, valid_time
from predictor import predict1
from multiprocessing.pool import ThreadPool
import json
from news_scraper import scraper
from summarize import Summarize
from extractTicker import stock_graph
from AltException import InvalidQuery, InvalidTicker

app = FastAPI()

@app.websocket("/ws")
async def websocket_handler(ws: WebSocket):
    await ws.accept()
    while True:
        query = await ws.receive_text()

        if query is None or query == "":
            await ws.send_json({"message": "Invalid query"})
            await ws.close(code=1003)
            break

        try:
            news = scraper(query)
            news_score = predict1(query, news.results).final_pred
        except InvalidQuery as e:
            await ws.send_json({"message": str(e)})
            await ws.close(code=1003)
            break

        pool = ThreadPool(processes=4)
        inter1 = pool.apply_async(pre, (1, news_score))
        inter7 = pool.apply_async(pre, (7, news_score))
        inter15 = pool.apply_async(pre, (15, news_score))
        inter30 = pool.apply_async(pre, (30, news_score))

        list_predicted = {}
        list_predicted[1] = inter1.get()
        list_predicted[7] = inter7.get()
        list_predicted[15] = inter15.get()
        list_predicted[30] = inter30.get()

        try:
            stg = stock_graph(query, [list_predicted[i] for i in [1, 7, 15, 30]])
        except InvalidTicker as e:
             await ws.send_json({"message": str(e)})
             await ws.close(code=1003)
             break

        responseObj = {
            "predictedPrice": {
                1: stg.predict_price_value.iloc[1]["price"],
                7: stg.predict_price_value.iloc[2]["price"],
                15: stg.predict_price_value.iloc[3]["price"],
                30: stg.predict_price_value.iloc[4]["price"],
            },
            "graph": stg.graphSocket(),
            "summary": Summarize(news.get_title(), 3).generate_summary()
        }

        await ws.send_json(responseObj)
        await ws.close(code=1000)
        break
