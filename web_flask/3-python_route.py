#!/usr/bin/python3
"""Underscore handling"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Prints Hello HBNB"""
    return "Hello HBNB"


@app.route('/hbnb')
def hbnb():
    """Prints HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """Prints the <text> variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def pyth(text="is cool"):
    """Prints <text>"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, use_reloader=True)
