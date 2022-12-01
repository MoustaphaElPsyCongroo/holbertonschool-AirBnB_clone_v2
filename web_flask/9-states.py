#!/usr/bin/python3
"""Flask web app with two routes: one for all states, another for one state"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>')
def display_states_or_state(id=None):
    states = storage.all(State)

    if id is not None:
        id = "State.{}".format(id)

    return render_template('9-states.html', states=states, state_id=id)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000, use_reloader=True)
