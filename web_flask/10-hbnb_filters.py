#!/usr/bin/python3
"""module 222"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Closes the SQLAlchemy session after each request."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a filtered list of States and Cities."""
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    amenities = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
