import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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