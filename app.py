import numpy as np
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression as LR
import matplotlib.pyplot as plt 
import os
from PIL import Image

X = np.linspace(1,100,1001).reshape(-1,1) 
y = 3 + 2*X + 50 * np.sin(X/5)

model = LR().fit(X,y)

app = Flask(__name__)

@app.route('/select', methods = ['GET', 'POST'])
def select():
    vocab = ['fruit','berry','rose','apple', 'banana', 'aromatic','rich']
    return render_template('select.html', vocab = vocab)

@app.route('/inputs', methods = ['GET','POST'])
def inputs():

    descriptors = [request.values['description'+str(i)] for i in range(5)]

    return ' '.join(descriptors)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/data')
def data():
    plt.scatter(X,y)
    plt.savefig('static/data.png')
    plt.close()

    return '<img src=static/data.png>'


@app.route('/predict')
def predict():
    x = np.array(np.random.random()).reshape(1,1)
    prediction = model.predict(x)

    return f'{x} is predicted to be {prediction}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)