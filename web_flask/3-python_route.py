#!/usr/bin/python3
"""
This Flask web application demonstrates how to handle different routes
and parameters. It provides simple string responses for various endpoints.

Modules:
    flask: The Flask framework used to create the web application.

Routes:
    /         : Returns a simple greeting 'hello HBNB'.
    /hbnb     : Returns 'HBNB'.
    /c/<text> : Returns 'C' followed by a dynamic text, replacing 
                underscores with spaces.
    /python/  : Returns 'Python is cool' by default or 'Python is <text>'
                if a text parameter is provided, replacing underscores 
                with spaces.
"""

from flask import Flask

# Create an instance of the Flask class for our web app
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """ 
    Home route handler.

    Returns:
        str: A simple greeting message 'hello HBNB'.
    """
    return 'hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ 
    HBNB route handler.

    Returns:
        str: A simple response 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ 
    C route handler with dynamic text.

    Args:
        text (str): The dynamic text provided in the URL.

    Returns:
        str: A formatted string 'C <text>' where underscores in 'text'
             are replaced by spaces.
    """
    text_with_no_slashes = text.replace('_', ' ')
    return f"C {text_with_no_slashes}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text='is_cool'):
    """
    Python route handler with dynamic text.

    Args:
        text (str): Optional dynamic text provided in the URL. Defaults
                    to 'cool' if not provided.

    Returns:
        str: A formatted string 'Python is <text>' where underscores
             in 'text' are replaced by spaces.
    """
    text_with_no_underscore = text.replace('_', ' ')
    return f"Python {text_with_no_underscore}"


if __name__ == '__main__':
    # Run the Flask application on host '0.0.0.0' and port 5000
    app.run(host='0.0.0.0', port=5000)
