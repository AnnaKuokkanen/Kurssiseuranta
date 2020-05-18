from CourseEditor import app, db
from flask import redirect, render_template, request, url_for
from CourseEditor.courses.models import Course

@app.route("/courses/courses.html", methods=["GET"])
def courses_list():
    return render_template("courses/courses.html", courses = Course.query.all())

@app.route("/courses/grades.html") 
def grades_show():
    return render_template("courses/grades.html")

@app.route("/courses/new.html")
def courses_form():
    return render_template("courses/new.html")

@app.route("/courses/new.html", methods=["POST"])
def courses_create():
    c = Course(request.form.get("name"), 
            request.form.get("content"), 
            request.form.get("time"))
        
    db.session().add(c)
    db.session().commit()

    return redirect(url_for("courses_list"))

@app.route("/courses/update.html/<course_id>", methods=["GET"])
def courses_update_form(course_id):
    return render_template("courses/update.html")

@app.route("/courses/update.html/<course_id>", methods=["POST"])
def courses_update(course_id):
    c = Course.query.get(course_id)
    c.name = request.form.get("name")
    c.content = request.form.get("content")
    c.time = request.form.get("time")

    db.session().commit()

    return redirect(url_for("courses_list"))