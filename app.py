from flask import Flask, render_template


app = Flask(__name__)


@app.route("/") #127.0.0.1:5000/
def index():
    return render_template("index.html")


if __name__== "__main__":
    app.run()