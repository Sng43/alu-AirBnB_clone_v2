#!/usr/bin/python3
"""This one will take parameters"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """ Home route """
    return 'hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB route """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ c route with dynamic text """
    text_with_no_slashes = text.replace('_', ' ')
    return f"C {text_with_no_slashes}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
