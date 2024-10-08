#!/usr/bin/python3
"""
This Flask web application contains routes that display simple text
responses. It demonstrates routing with dynamic parameters and how
to structure a basic Flask app.

Modules:
    flask: The Flask class and request handling for creating the web app.

Routes:
    /         : Returns a simple "hello HBNB" message.
    /hbnb     : Returns a simple "HBNB" message.
    /c/<text> : Returns a message "C" followed by a dynamic text, with 
                underscores in the text replaced by spaces.
"""

from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """
    Home route handler.

    Returns:
        str: A string response 'hello HBNB'.
    """
    return 'hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    HBNB route handler.

    Returns:
        str: A string response 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    Dynamic C route handler.

    Args:
        text (str): The dynamic part of the URL after '/c/'.
                    Underscores in this text will be replaced with spaces.

    Returns:
        str: A formatted string 'C <text>' where underscores in 'text' are replaced by spaces.
    """
    # Replace underscores with spaces in the dynamic text
    text_with_no_slashes = text.replace('_', ' ')
    return f"C {text_with_no_slashes}"


if __name__ == '__main__':
    # Run the Flask app on host '0.0.0.0' and port 5000
    app.run(host='0.0.0.0', port=5000)
