from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World this is just a practice test!'


if __name__ == '__main__':
    app.run(debug=True)