from CourseEditor import app, db
from CourseEditor.users.forms import LoginForm
from CourseEditor.users.models import User
from flask import render_template, request, url_for, redirect

@app.route("/users/login.html")
def users_login():
    return render_template("users/login.html", form = LoginForm())

@app.route("/users/login.html", methods=["POST"])
def users_login_form():
    form = LoginForm(request.form)
    user = User.query.filter_by(username = form.username.data, password = form.password.data).first()
    if not user:
        return render_template("users/login.html", form = form, 
                                error = "Käyttäjää ei löydy")

    print("Käyttäjä " + user.username + " tunnistettiin")
    return redirect(url_for("users_menu"))

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

