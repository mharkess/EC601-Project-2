from flask import Flask, render_template

app = Flask("TwitterBot")

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/about/")
def About():
    return render_template("about.html")