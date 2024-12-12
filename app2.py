from flask import Flask, render_template, request
from processing import get_prediction

app = Flask(__name__)


@app.route("/", methods=["get", "post"]) #127.0.0.1:5000/
def index():
    message = ""
    if request.method == "POST":
        area = request.form.get("area")
        try:
            area = float(area)
            cost = get_prediction(area)
            message = f"Результатом по ОКПД 2 равным  {area} является {cost}"
        except:
            message = f"Введено что-то не верное: {area}"
    return render_template("index2.html", message = message)


if __name__== "__main__":
    app.run()