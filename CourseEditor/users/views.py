from CourseEditor import app, db
from CourseEditor.users.forms import LoginForm, RegistrationForm
from CourseEditor.users.models import User
from flask import render_template, request, url_for, redirect
from flask_login import login_required, login_user, logout_user

@app.route("/users/login.html")
def users_login():
    return render_template("users/login.html", form = LoginForm())

@app.route("/users/login.html", methods=["POST"])
def users_login_form():
    form = LoginForm(request.form)

    if not form.validate():
        return render_template("users/login.html", form = form)

    user = User.query.filter_by(username = form.username.data, password = form.password.data).first()
    if not user:
        return render_template("users/login.html", form = form, 
                                error = "Käyttäjää ei löydy")

    print("Käyttäjä " + user.username + " tunnistettiin")
    login_user(user)
    return redirect(url_for("users_menu"))

@app.route("/users/logout")
def users_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/users/menu.html")
@login_required
def users_menu():
    return render_template("users/menu.html")

@app.route("/users/new.html")
def users_form():
    return render_template("users/new.html", form = RegistrationForm())

@app.route("/users/new.html", methods=["POST"])
def users_create():
    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("users/new.html", form = form)
    
    u = User.query.filter_by(username = form.username.data).first()
    if u:
        return render_template("users/new.html", form = form, 
                                error = "Käyttäjänimi käytössä")
    else:
        u = User(form.firstname.data,
                form.lastname.data,
                form.username.data,
                form.password.data)

        db.session().add(u)
        db.session().commit()
    
        return render_template("/index.html")

