from CourseEditor import app
from flask import render_template, request

@app.route("/users/new.html")
def tasks_form():
    return render_template("users/new.html")

@app.route("/users/", methods=["POST"])
def users_create():
    print(request.form.get("fname"))
    print(request.form.get("lname"))
    print(request.form.get("user"))
    print(request.form.get("pin"))
  
    return "Kiitos!"