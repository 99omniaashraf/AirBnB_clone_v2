#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ def doc """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces in the text variable
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ def doc """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ def doc """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """ def doc """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
