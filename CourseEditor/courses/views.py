from CourseEditor import app, db
from CourseEditor.courses.models import Course
from CourseEditor.courses.forms import NewForm, SearchForm, UpdateForm
from flask import redirect, render_template, request, url_for

@app.route("/courses/courses.html", methods=["GET"])
def courses_list():
    return render_template("courses/courses.html", form = SearchForm(), courses = Course.query.all())

@app.route("/course/courses.html", methods=["POST"])
def courses_search():
    form = SearchForm(request.form)
    
    if not form.validate():
        return render_template("courses/courses.html", form = form)

    return render_template("courses/list.html", courses = Course.query.filter_by(name=form.name.data))

@app.route("/course/courses.htl/<course_id>", methods=["POST"])
def courses_delete(course_id):
    c = Course.query.get(course_id)
    db.session.delete(c)
    db.session().commit()

    return redirect(url_for("courses_list"))

@app.route("/courses/grades.html") 
def grades_show():
    return render_template("courses/grades.html")

@app.route("/courses/new.html")
def courses_form():
    return render_template("courses/new.html", form = NewForm())

@app.route("/courses/new.html", methods=["POST"])
def courses_create():
    form = NewForm(request.form)
    c = Course(form.name.data, 
            form.content.data, 
            form.time.data)
        
    db.session().add(c)
    db.session().commit()

    return redirect(url_for("courses_list"))

@app.route("/courses/update.html/<course_id>", methods=["GET"])
def courses_update_form(course_id):
    id = course_id
    return render_template("courses/update.html", form = UpdateForm(), course = Course.query.get(id))

@app.route("/courses/update.html/<course_id>", methods=["POST"])
def courses_update(course_id):
    form = UpdateForm(request.form)
    c = Course.query.get(course_id)
    c.name = form.name.data
    c.content = form.content.data
    c.time = form.time.data

    db.session().commit()

    return redirect(url_for("courses_list"))