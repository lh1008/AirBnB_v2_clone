#!/usr/bin/python3
""" Module script that startsa Flask web application """
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """ Method that returns displayed message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ Method routing to hbnb decorator """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ Method that displays C followed by value """
    return 'C %s' % escape(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
