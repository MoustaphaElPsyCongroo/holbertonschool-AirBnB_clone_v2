#!/usr/bin/python3
"""Displays a list of states using Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list")
def list_states():
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000, use_reloader=True)
