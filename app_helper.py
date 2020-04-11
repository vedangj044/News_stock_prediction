import numpy as np
from sklearn.linear_model import LinearRegression


def pre(delta, r):

    with open('fuck1.txt', 'r') as values:
        data = eval(values.read())

    X = []
    Y = []

    pos = False
    if r > 0.5:
        # triggered only when news articles are negative
        pos = True # pragma: no cover

    for i in range(len(data)):
        if pos and data[i][0] >= 0.5:
            X.append(round(data[i][0], 5)) # pragma: no cover
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
