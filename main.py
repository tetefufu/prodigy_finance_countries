from flask import Flask

app = Flask(__name__)

@app.route("/")
def get():
    return "It Works"

if __name__ == "__main__":
    app.run(debug=True)