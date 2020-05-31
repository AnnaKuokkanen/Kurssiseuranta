from CourseEditor import app, db
from CourseEditor.courses.forms import NewForm, SearchForm, UpdateForm
from CourseEditor.courses.models import Course
from CourseEditor.teachers.models import Teacher
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
    #Not ready, write a custom query

    #course_account = UserCourse.query.filter_by(course_id=course_id, user_id=current_user.id)

    #db.session.delete(course_account)
    #db.session().commit()

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
    
    c = Course.query.filter_by(name=form.name.data, content=form.content.data, time=form.time.data).first()

    if c is None:
        c = Course(form.name.data, 
                form.content.data, 
                form.time.data)

        t = Teacher.query.filter_by(firstname=form.teacher_firstname.data, lastname=form.teacher_lastname.data).first()

        if t is None:
            t = Teacher(form.teacher_firstname.data,
                    form.teacher_lastname.data
            )
            db.session().add(t)
            db.session().commit()
            t = Teacher.query.filter_by(firstname=form.teacher_firstname.data, lastname=form.teacher_lastname.data).first()
            c.teacher_id = t.id
        else: 
            c.teacher_id = t.id

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
    t = Teacher.query.get(c.teacher_id)

    c.name = form.name.data
    c.content = form.content.data
    c.time = form.time.data
    t.firstname = form.teacher_firstname.data
    t.lastname = form.teacher_lastname.data

    db.session().commit()

    return redirect(url_for("courses_list"))