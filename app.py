#!/usr/bin/env python3

# local imports
import time
import logging
from flask import Flask, render_template

# create the flask application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def viewAbout():
    return render_template('about.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
