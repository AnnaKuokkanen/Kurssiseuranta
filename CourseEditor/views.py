from flask import render_template
from CourseEditor import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu.html")
def menu():
    return render_template("menu.html")

@app.route("/plan.html")
def plan():
    return render_template("plan.html")

@app.route("/grades.html")
def grades():
    return render_template("grades.html")

@app.route("/courses.html")
def courses():
    return render_template("courses.html")
