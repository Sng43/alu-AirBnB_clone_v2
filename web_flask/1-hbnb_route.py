#!/usr/bin/python3
"""This one will take parameters"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """
    
    """
    return 'hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    
    """
    return 'HBNB'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)