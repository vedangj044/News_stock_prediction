from flask import Flask, request, jsonify, session
from flask_cors import CORS
import json
from summarize import Summarize
from news_scraper import scraper

app = Flask(__name__)
CORS(app)


@app.route('/news', methods=['POST'])
def sentiment_analyzer():
    '''
    Receives company name and send back json response ['Positive', 'Negative']
    '''
    query = request.form.get('query')

    l = [0.004,0.23,1.23,2.5]
    s = """{'$schema': 'https://vega.github.io/schema/vega-lite/v4.0.2.json',
        'config': {'view': {'continuousHeight': 300, 'continuousWidth': 400}},
        'data': {'name': 'data-c2a3e89ba9d5d1687d5e8c28d630a033'},
        'datasets': {'data-c2a3e89ba9d5d1687d5e8c28d630a033': [{'a': 'A', 'b': 28},
        {'a': 'B', 'b': 55},
        {'a': 'C', 'b': 43},
        {'a': 'D', 'b': 91},
        {'a': 'E', 'b': 81},
        {'a': 'F', 'b': 53},
        {'a': 'G', 'b': 19},
        {'a': 'H', 'b': 87},
        {'a': 'I', 'b': 52}]},
        'encoding': {'x': {'field': 'a', 'type': 'nominal'},
        'y': {'field': 'b', 'type': 'quantitative'}},
        'mark': 'bar'}"""
    p = "https://freedesignfile.com/upload/2018/01/Shiny-stars-light-with-triangle-abstract-background-vector-12.jpg"    
    resp = {"predict": l, "graph": s, "image": p}
    return json.dumps(resp)

@app.route('/get_summary', methods=["GET"])
def get_summary():
    news = scraper(session['query']).get_title()
    test_file = open('summary.txt', 'w')
    test_file.write(news)
    test_file.close()
    pointers = 3
    try:
        summary = Summarize('summary.txt', pointers).generate_summary()
    except:
        return("Articles are short. Unable to get sufficient pointers")
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=False)

