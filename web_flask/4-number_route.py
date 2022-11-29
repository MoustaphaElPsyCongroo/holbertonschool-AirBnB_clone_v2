#!/usr/bin/python3
"""Integer module"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


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
    return f"C {text.replace('_', ' ')}"


@app.route('/python')
@app.route('/python/<text>')
def pyth(text="is cool"):
    """Prints <text>"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def num(n):
    """Prints n if it's an int"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
