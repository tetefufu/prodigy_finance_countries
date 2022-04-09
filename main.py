from flask import Flask

app = Flask(__name__)


@app.route("/")
def get():
    return '{"books": "it works"}'


if __name__ == "__main__":
    app.run(debug=True)
