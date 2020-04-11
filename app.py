from flask import Flask, request, jsonify, session
from flask_cors import CORS
from summarize import Summarize
from predictor import predict1
import json
from multiprocessing.pool import ThreadPool
from extractTicker import stock_graph
from news_scraper import scraper
from app_helper import pre


app = Flask(__name__)
CORS(app)
SESSION_TYPE = 'redis'
app.config['SECRET_KEY'] = "THIS IS SECRET"
app.config.from_object(__name__)


@app.route('/news', methods=['POST'])
def sentiment_analyzer():
    '''
    Returns the change in value in interval of days.
    '''
    query = request.form.get('query')

    if query is None:
        return json.dumps({"Message": "Send query in formdata"})

    list_predicted = {}
    news_score = predict1(query).final_pred

    pool = ThreadPool(processes=4)
    inter1 = pool.apply_async(pre, (1, news_score))
    inter7 = pool.apply_async(pre, (7, news_score))
    inter15 = pool.apply_async(pre, (15, news_score))
    inter30 = pool.apply_async(pre, (30, news_score))

    list_predicted["1"] = inter1.get()
    list_predicted["7"] = inter7.get()
    list_predicted["15"] = inter15.get()
    list_predicted["30"] = inter30.get()

    session['query'] = query
    session['list_predicted'] = list_predicted

    return json.dumps({"predict": list_predicted})


@app.route('/stock-graph', methods=['GET'])
def graph():

    list_predicted = session.pop('list_predicted')
    graph_pre = [list_predicted["1"],
                 list_predicted["7"],
                 list_predicted["15"],
                 list_predicted["30"]]

    return stock_graph(session['query'],
                       graph_pre).graph()


@app.route('/get-summary/', methods=["GET"])
def get_summary():

    news = scraper(session['query']).get_title()
    pointers = 3
    return jsonify(Summarize(news, pointers).generate_summary())


if __name__ == '__main__':
    app.run(debug=True) # pragma: no cover
