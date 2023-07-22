#!/usr/bin/python3
"""
This is a Flask web application that:
1. Listens on 0.0.0.0:5000
2. Route / displays "Hello HBNB!"
3. Route /hbnb that displays "HBNB"
4. Route /c/<text> displays C followed by text
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
    This route /displays "HBNB!"
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cprint(text):
    """
    This route /c/<text> displays C followed by value of text variable
    """
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
