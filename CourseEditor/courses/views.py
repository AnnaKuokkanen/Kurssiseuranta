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
    return render_template("courses/courses.html", form = SearchForm(), courses = Course.list_course_and_teacher(current_user.id))

@app.route("/course/courses.html", methods=["POST"])
@login_required
def courses_search():
    form = SearchForm(request.form)

    if not form.validate():
        return render_template("courses/courses.html", form = form)

    return render_template("courses/list.html", courses = Course.find_course_and_teacher(current_user.id, form.name.data))

@app.route("/course/courses.html/<course_id>", methods=["POST"])
@login_required
def courses_delete(course_id):

    User.remove_row(current_user.id, course_id)
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
    
    c = Course.query.filter_by(name=form.name.data, content=form.content.data, time=form.time.data).first()
    t = Teacher.query.filter_by(firstname=form.teacher_firstname.data, lastname=form.teacher_lastname.data).first()

    return create_or_update(c, t, form.teacher_firstname.data, form.teacher_lastname.data, form.name.data, form.content.data, form.time.data)

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

    t = Teacher.query.filter_by(firstname=form.teacher_firstname.data, lastname=form.teacher_lastname.data).first()
    c = Course.query.filter_by(name=form.name.data, content=form.content.data, time=form.time.data).first()

    User.remove_row(current_user.id, id)
    
    return create_or_update(c, t, form.teacher_firstname.data, form.teacher_lastname.data, form.name.data, form.content.data, form.time.data)

def create_or_update(c, t, teacher_firstname, teacher_lastname, course_name, course_content, course_time):

    if t is None:
        t = Teacher(teacher_firstname,
                    teacher_lastname)

        db.session().add(t)
        db.session().commit()

    if c is None:
        c = Course(course_name, 
            course_content, 
            course_time)
        c.teacher_id = t.id

        db.session().add(c)
    
        c.accounts.append(current_user)
        current_user.courses.append(c)

        db.session().commit()

        return redirect(url_for("courses_list"))

    course_id = Course.check_if_course_and_teacher_exist(t.id, course_name, course_content, course_time)

    if not course_id:
        c = Course(course_name, 
                    course_content, 
                    course_time)
        c.teacher_id = t.id

        db.session().add(c)

    elif course_id:
        c = Course.query.get(course_id[0])
        
    c.accounts.append(current_user)
    current_user.courses.append(c)

    db.session().commit()

    return redirect(url_for("courses_list"))