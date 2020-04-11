from flask import Flask, request, jsonify, session
from flask_cors import CORS
from summarize import Summarize
from predictor import predict1
import json
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

    list_predicted = []
    news_score = predict1(query).final_pred

    for i in [1, 7, 15, 30]:
        value_of_pre = pre(i, news_score).tolist()[0]*100
        list_predicted.append(value_of_pre)

    session['query'] = query
    session['list_predicted'] = list_predicted

    return json.dumps({"predict": list_predicted})


@app.route('/stock-graph', methods=['GET'])
def graph():

    return stock_graph(session['query'],
                       session.pop('list_predicted')).graph()


@app.route('/get-summary/', methods=["GET"])
def get_summary():

    news = scraper(session['query']).get_title()
    pointers = 3
    return jsonify(Summarize(news, pointers).generate_summary())


if __name__ == '__main__':
    app.run(debug=True) # pragma: no cover
