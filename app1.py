from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["get", "post"]) #127.0.0.1:5000/
def index():
    message = ""
    if request.method == "POST":
        area = request.form.get("area")
        message = f"Введено что-то нужное: {area}"
    return render_template("index1.html", message = message)


if __name__== "__main__":
    app.run()