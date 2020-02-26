import numpy as np
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    vocab = ['shoelace','manure','soap','formaldehyde','brimstone']
    values = [1,2,3,4,5]
    return render_template('select.html', vocab = vocab, values = values)

@app.route('/result', methods = ['GET','POST'])
def inputs():
    columns = [request.values['description'+str(i)] for i in range(5)]
    values = [request.values['value'+str(i)] for i in range(5)]

    ideal_wine = pd.DataFrame({c:[v] for c,v in zip(columns,values)})

    return f'Your favorite flavor profile: {ideal_wine}. <br> Perhaps you might enjoy this wine: "X" which is was rated 85 points by Hannibal Lecter'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)