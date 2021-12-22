# Python Flask aplikacija

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/onama")
def o_nama():
    return render_template("onama.html")

@app.route("/proizvodi")
def proizvodi():
    return render_template("proizvodi.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(use_reloader=True)