#!/usr/bin/python3
"""Flask web app with 3 routes & one variable"""
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
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, use_reloader=True)
