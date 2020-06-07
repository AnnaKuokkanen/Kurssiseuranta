from CourseEditor import app
from CourseEditor.courses.models import Course
from flask import render_template
from flask_login import current_user, login_required

@app.route("/grades/grades.html") 
@login_required
def grades_show():
    return render_template("grades/grades.html", grades = Course.list_course_and_teacher(current_user.id))