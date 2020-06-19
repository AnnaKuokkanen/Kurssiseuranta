from CourseEditor import app, db, login_required
from CourseEditor.courses.forms import CourseForm, SearchForm
from CourseEditor.courses.models import Course
from CourseEditor.teachers.models import Teacher
from CourseEditor.usercourse.models import UserCourse
from CourseEditor.users.models import User
from flask import redirect, render_template, request, url_for
from flask_login import current_user

@app.route("/courses/courses.html", methods=["GET"])
@login_required
def courses_list():
    courses = Course.list_course_and_teacher(current_user.id)
    return render_template("courses/courses.html", form = SearchForm(), courses = courses)

@app.route("/course/courses.html", methods=["POST"])
@login_required
def courses_search():
    form = SearchForm(request.form)

    if not form.validate():
        return render_template("courses/courses.html", form = form)

    return render_template("courses/list.html", courses = Course.find_course_and_teacher(current_user.id, form.name.data))

@app.route("/course/courses.html/<course_id>", methods=["POST"])
@login_required()
def courses_delete(course_id):
    User.remove_row(current_user.id, course_id)
    db.session().commit()

    return redirect(url_for("courses_list"))

@app.route("/course/info.html/<course_id>", methods=["GET"])
@login_required()
def course_info(course_id):

    return render_template("courses/info.html", students = Course.list_students(course_id))

@app.route("/courses/new.html")
@login_required
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/new.html", methods=["POST"])
@login_required
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form = form)
    
    c = Course.query.filter_by(name=form.name.data, content=form.content.data, time=form.time.data).first()
    t = Teacher.query.filter_by(firstname=form.teacher_firstname.data, lastname=form.teacher_lastname.data).first()
    completed = form.completed.data
    planned = form.planned.data

    return create_or_update(c, t, form.teacher_firstname.data, form.teacher_lastname.data, form.name.data, form.content.data, form.time.data, completed, planned)

@app.route("/courses/update.html/<course_id>", methods=["GET"])
@login_required
def courses_update_form(course_id):
    c = Course.query.get(course_id)
    t = Teacher.query.get(c.teacher_id)
    course = {'name': c.name, 'content': c.content, 'time': c.time, 'teacher_firstname': t.firstname, 'teacher_lastname': t.lastname}
    return render_template("courses/update.html", form = CourseForm(data=course), course = Course.query.get(course_id))

@app.route("/courses/update.html/<course_id>", methods=["POST"])
@login_required()
def courses_update(course_id):
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/update.html", form = form, course = Course.query.get(course_id))

    c = Course.query.filter_by(name=form.name.data, content=form.content.data, time=form.time.data).first()
    t = Teacher.query.filter_by(firstname=form.teacher_firstname.data, lastname=form.teacher_lastname.data).first()
    completed = form.completed.data
    planned = form.planned.data

    User.remove_row(current_user.id, course_id)
    db.session().commit()
    
    return create_or_update(c, t, form.teacher_firstname.data, form.teacher_lastname.data, form.name.data, form.content.data, form.time.data, completed, planned)

def create_or_update(c, t, teacher_firstname, teacher_lastname, course_name, course_content, course_time, completed, planned):

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
        db.session().commit()
    
        uc = UserCourse(current_user.id, c.id, completed, planned)
        db.session.add(uc)
        db.session().commit()

        return redirect(url_for("courses_list"))

    course_id = Course.check_if_course_and_teacher_exist(t.id, course_name, course_content, course_time)

    if not course_id:
        c = Course(course_name, 
                    course_content, 
                    course_time)
        c.teacher_id = t.id

        db.session().add(c)
        db.session().commit()

    else:
        c = Course.query.get(course_id[0])

    uc = UserCourse.query.filter_by(user_id=current_user.id, course_id=c.id).first()
    if uc is None:
        uc = UserCourse(current_user.id, c.id, completed, planned)
        db.session().add(uc)
  
    db.session().commit()

    return redirect(url_for("courses_list"))