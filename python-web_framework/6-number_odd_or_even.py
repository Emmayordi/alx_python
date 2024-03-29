from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return "C {}".format(text.replace('_', ' '))

@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is_cool'):
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('6-number_template.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n, odd_even='odd' if n % 2 != 0 else 'even')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
