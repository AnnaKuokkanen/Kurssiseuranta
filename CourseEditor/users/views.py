from CourseEditor import app, db, login_required
from CourseEditor.users.forms import LoginForm, RegistrationForm, UpdateForm
from CourseEditor.users.models import User
from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_user, logout_user

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
    
    user = User.query.filter_by(username = form.username.data).first()
    admin = 1
    
    if form.admin.data:
        admin = 2

    if user:
        return render_template("users/new.html", form = form, 
                                error = "Käyttäjänimi käytössä")
    else:
        user = User(form.firstname.data,
                form.lastname.data,
                form.username.data,
                form.password.data, admin)

        db.session().add(user)
        db.session().commit()
    
        return render_template("/index.html")

@app.route("/users/profile.html", methods=["GET"])
@login_required
def show_profile():
    return render_template("users/profile.html", user = User.query.get(current_user.id))

@app.route("/users/users.html", methods=["GET"])
@login_required(role="ADMIN")
def show_users():
    return render_template("users/users.html", users = User.list_all_users())

@app.route("/users/users.html/<user_id>", methods=["POST"])
@login_required(role="ADMIN")
def make_admin(user_id):
    user = User.query.get(user_id)
    user.role_id = 2
    db.session().add(user)
    db.session().commit()
    return redirect(url_for("show_users"))

@app.route("/users/statistics.html", methods=["GET"])
@login_required(role="ADMIN")
def show_stats():
    return render_template("users/statistics.html", stats = User.count_statistics(current_user.id))

@app.route("/users/profile.html/<user_id>", methods=["POST"])
@login_required
def delete_profile(user_id):
    logout_user()
    User.remove_user(user_id)
    u = User.query.get(user_id)
    db.session().delete(u)
    db.session().commit()

    return redirect(url_for("index"))

@app.route("/users/update.html/<user_id>", methods=["GET"])
@login_required
def update_profile_form(user_id):
    u = User.query.get(user_id)
    user = {'firstname': u.firstname, 'lastname': u.lastname}
    return render_template("users/update.html", form=UpdateForm(data=user), user = User.query.get(user_id))

@app.route("/users/update.html/<user_id>", methods=["POST"])
@login_required
def update_profile(user_id):
    form = UpdateForm(request.form)

    if not form.validate():
        return render_template("users/update.html", form=form, user = User.query.get(user_id))

    u = User.query.get(user_id)
    u.firstname = form.firstname.data
    u.lastname = form.lastname.data
    db.session().add(u)
    db.session().commit()

    return render_template("users/profile.html", user = User.query.get(user_id))