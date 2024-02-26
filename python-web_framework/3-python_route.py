"""
3-python_route.py
Starts a Flask web application.

Web application listens on 0.0.0.0, port 5000.
Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    /c/<text>: display "C ", followed by the value of the text variable (replace underscore _ symbols with a space)
    /python/<text>: display "Python ", followed by the value of the text variable (replace underscore _ symbols with a space)
    Default value of text is "is cool"
"""

from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" when the root route is accessed.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" when the /hbnb route is accessed.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays "C ", followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return 'C {}'.format(escape(text.replace('_', ' ')))

@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is_cool'):
    """
    Displays "Python ", followed by the value of the text variable.
    Replace underscore _ symbols with a space. Default value of text is "is cool".
    """
    return 'Python {}'.format(escape(text.replace('_', ' ')))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)