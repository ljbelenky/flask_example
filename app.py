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

# Get the description words (flavors) from request and put in a list
    columns = [request.values['description'+str(i)] for i in range(5)]
# Get the values from request and put in a list
    values = [request.values['value'+str(i)] for i in range(5)]
# Combine flavors and values to create a pandas DataFrame describing your ideal wine
    ideal_wine = pd.DataFrame({c:[v] for c,v in zip(columns,values)})

    return f'Your favorite flavor profile: {ideal_wine}. <br> Perhaps you might enjoy this wine: "X" which is was rated 85 points by Hannibal Lecter'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)