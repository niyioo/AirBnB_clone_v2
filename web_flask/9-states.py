#!/usr/bin/python3
"""module"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Closes the SQLAlchemy session after each request."""
    storage.close()

@app.route('/states', strict_slashes=False)
def states():
    """Display a list of states."""
    states = sorted(list(storage.all(State).values()), key=lambda state: state.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """Display cities for a specific state or 'Not found'."""
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', not_found=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

