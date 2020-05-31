from CourseEditor import app, db
from CourseEditor.courses.forms import NewForm, SearchForm, UpdateForm
from CourseEditor.courses.models import Course
from CourseEditor.usercourse.models import UserCourse
from CourseEditor.users.models import User
from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

@app.route("/courses/courses.html", methods=["GET"])
@login_required
def courses_list():
    return render_template("courses/courses.html", form = SearchForm(), courses = current_user.courses)

@app.route("/course/courses.html", methods=["POST"])
@login_required
def courses_search():
    form = SearchForm(request.form)

    if not form.validate():
        return render_template("courses/courses.html", form = form)

    return render_template("courses/list.html", courses = Course.query.filter_by(name=form.name.data))

@app.route("/course/courses.html/<course_id>", methods=["POST"])
@login_required
def courses_delete(course_id):
    course_account = UserCourse.query.filter_by(course_id=course_id, user_id=current_user.id)

    db.session.delete(course_account)
    db.session().commit()

    return redirect(url_for("courses_list"))

@app.route("/courses/grades.html") 
@login_required
def grades_show():
    return render_template("courses/grades.html")

@app.route("/courses/new.html")
@login_required
def courses_form():
    return render_template("courses/new.html", form = NewForm())

@app.route("/courses/new.html", methods=["POST"])
@login_required
def courses_create():
    form = NewForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form = form)

    c = Course(form.name.data, 
            form.content.data, 
            form.time.data)

    c.accounts.append(current_user)
    current_user.courses.append(c)
    db.session().add(c)
    
    db.session().commit()

    return redirect(url_for("courses_list"))

@app.route("/courses/update.html/<course_id>", methods=["GET"])
@login_required
def courses_update_form(course_id):
    id = course_id
    return render_template("courses/update.html", form = UpdateForm(), course = Course.query.get(id))

@app.route("/courses/update.html/<course_id>", methods=["POST"])
@login_required
def courses_update(course_id):
    id = course_id
    form = UpdateForm(request.form)

    if not form.validate():
        return render_template("courses/update.html", form = form, course = Course.query.get(id))

    c = Course.query.get(course_id)
    c.name = form.name.data
    c.content = form.content.data
    c.time = form.time.data

    db.session().commit()

    return redirect(url_for("courses_list"))