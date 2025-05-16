from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    """Return a friendly HTTP greeting.

    Returns:
        A string with a random number from a list.
    """
    return str(random.choice([5, 10, 12, 8, 9, 2]))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
