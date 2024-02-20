#!usr/bin/python3

"""
Starts a Flask web application.
The application listens on O.O.O.O, port 5OOO
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
