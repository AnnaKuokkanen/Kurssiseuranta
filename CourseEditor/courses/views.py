from CourseEditor import app, db
from flask import render_template, request
from CourseEditor.courses.models import Course

@app.route("/courses/grades.html") 
def grades_show():
    return render_template("courses/grades.html")

@app.route("/courses/new.html")
def courses_form():
    return render_template("courses/new.html")

@app.route("/courses/courses.html", methods=["GET"])
def courses_list():
    return render_template("courses/courses.html", courses = Course.query.all())

@app.route("/courses/new.html", methods=["POST"])
def courses_create():
    c = Course(request.form.get("name"), 
            request.form.get("content"), 
            request.form.get("time"))
        
    db.session().add(c)
    db.session().commit()

    return render_template("courses/courses.html")
