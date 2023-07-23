#!/usr/bin/python3
"""
This is a Flask web application that:
1. Listens on 0.0.0.0:5000
2. Route / displays "Hello HBNB!"
3. Route /hbnb that displays "HBNB"
4. Route /c/<text> displays C followed by text
5. Route /python/<text> that displays Python and text value
6. Displays "is cool" as default value of text
7. Route /number/<n> displays 'n is a number' if n is an integer
8. Add route /number_template/<n> display HTML only if n is an integer
9. Add /number_odd_or_even/<n> route displays HTML if n is a number
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def airbnb():
    """
    This route / displays "Hello HBNB!"
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This route /hbnb displays "HBNB!"
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def printx(text):
    """
    This route /c/<text> displays C followed by value of text variable
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def printpyth(text="is cool"):
    """
    This route /python/<text> displays Python followed by value of text variable
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def printz(n):
    """
        Route /number/<n> that displays 'n is a number' if n is an integer
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def ntemplate(n):
    """
        Route /number_template/<n> that displays webpage if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddeven(n):
    """
        Route /number_odd_or_even/<n> route displays HTML if n is a number
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
