#!/usr/bin/python3
"""
This is a Flask web application that:
1. Listens on 0.0.0.0:5000
2. Route / displays "Hello HBNB!"
3. Route /hbnb that displays "HBNB"
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def airbnb():
    """
        This Route / displays "Hello HBNB!"
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
       This Route /hbnb displays "HBNB!"
    """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
