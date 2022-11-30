#!/usr/bin/python3
"""Integer route"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """Starts a Flask web app"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Binds with hbnb"""
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


@app.route('/number/<int:n>')
def num(n):
    """Prints n if it's an int"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run("0.0.0.0", 5000, use_reloader=True)
