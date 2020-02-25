import numpy as np
from flask import Flask
from sklearn.linear_model import LinearRegression as LR

X = np.linspace(1,100,1001).reshape(-1,1)
y = 3 + 2*X + np.random.random()

model = LR().fit(X,y)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/data')
def data():
    return 'The Data: <br>' +'<br>'.join([f'{[xx[0], yy[0]]}' for xx, yy in zip(X,y)])

@app.route('/predict')
def predict():
    x = np.array(np.random.random()).reshape(1,1)
    prediction = model.predict(x)

    return f'{x} is predicted to be {prediction}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)