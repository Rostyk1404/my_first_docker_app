from flask import Flask
from random import randint

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/random_number')
def random_number():
    result = randint(1, 10)
    return str(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
