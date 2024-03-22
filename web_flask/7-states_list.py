#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display "HBNB" """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Display "C <text>" where underscores are replaced with spaces """
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Display "Python <text>" where underscores are replaced with spaces """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """ Display "<n> is a number" if n is an integer """
    if isinstance(n, int):
        return '{} is a number'.format(n)
    else:
        return "404 Not Found"


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def show_odd_or_even(n):
    if isinstance(n, int):
        if n % 2 == 0:
            p = 'even'
        else:
            p = 'odd'
        return render_template('6-number_odd_or_even.html', number=n, parity=p)
    else:
        return "404 Not Found"


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the current SQLAlchemy Session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of states sorted by name."""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
