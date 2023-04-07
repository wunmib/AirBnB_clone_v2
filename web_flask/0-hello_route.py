#!/usr/bin/python3
"""
    This script starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ returns Hello HBNB! when requested """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
