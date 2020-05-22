from CourseEditor import app, db
from flask import render_template, request
from CourseEditor.users.models import User

@app.route("/users/login.html")
def users_login():
    return render_template("users/login.html")

@app.route("/users/menu.html")
def users_menu():
    return render_template("users/menu.html")

@app.route("/users/new.html")
def users_form():
    return render_template("users/new.html")

@app.route("/users/new.html", methods=["POST"])
def users_create():
    u = User(request.form.get("username"),
            request.form.get("password"),
            request.form.get("firstname"),
            request.form.get("lastname"))

    db.session().add(u)
    db.session().commit()
  
    return render_template("/index.html")

