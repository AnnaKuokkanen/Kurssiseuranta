from CourseEditor import app
from flask import render_template

@app.route("/courses/courses.html") 
def courses_show():
    return render_template("courses/courses.html")

@app.route("/courses/grades.html") 
def grades_show():
    return render_template("courses/grades.html")