#!/usr/bin/python3
"""This one will take parameters"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """ 
    Home route 
    """
    return 'hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ 
    HBNB route 
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ 
    C route with dynamic text 
    """
    text_with_no_slashes = text.replace('_', ' ')
    return f"C {text_with_no_slashes}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text='is_cool'):
    """
    Python is fun
    """
    text_with_no_underscore = text.replace('_', ' ')
    return f"Python {text_with_no_underscore}"

@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """
    Python is fun
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    
    """
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
