from flask import Flask, request, jsonify
from flask_cors import CORS
from predictor import predict

app = Flask(__name__)
CORS(app)

API_URL = '/News_stock_prediction/api/v1/get_news'

@app.route(API_URL, methods=['POST'])
def sentiment_analyzer():
    '''
    Receives company name and send back json response ['Positive', 'Negative']
    '''
    company = request.form['company']

    res = predict(company).resp()

    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=False)
