from flask import Flask, request, jsonify
from flask_cors import CORS
from predictor import predict1
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import json
from extractTicker import stock_graph



app = Flask(__name__)
CORS(app)

API_URL = '/news'

def pre(delta, r):
    data = eval(open('fuck1.txt', 'r').read())
    X = []
    Y = []

    pos = False
    if r>0.5:
        pos = True

    for i in range(len(data)):
        if pos and data[i][0] >= 0.5: 
            X.append(round(data[i][0], 5))
        else:
            X.append(round(data[i][0], 5))

    X = np.array(X).reshape(-1, 1)

    if delta == 1:
        for i in range(len(data)):
            Y.append(round(data[i][1], 5))
    elif delta == 7:
        for i in range(len(data)):
            Y.append(round(data[i][2], 5))
    elif delta == 15:
        for i in range(len(data)):
            Y.append(round(data[i][3], 5))
    elif delta == 30:
        for i in range(len(data)):
            Y.append(round(data[i][4], 5))
    reg = LinearRegression()
    classi = reg.fit(X, Y)

    return classi.predict(np.array(r).reshape(1, -1))


@app.route('/news', methods=['POST'])
def sentiment_analyzer():
    '''
    Receives company name and send back json response ['Positive', 'Negative']

    '''
    query = request.form['company']

    l = []
    for i in [1, 7, 15, 30]:
        l.append(pre(i, predict1(query).final_pred).tolist()[0]*100)

    return json.dumps(l)

@app.route('/stock-graph', methods=['POST'])
def graph():
 
    s = stock_graph('tesla').get_history()
    return s 

if __name__ == '__main__':
    app.run(debug=False)
