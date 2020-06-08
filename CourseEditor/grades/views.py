from CourseEditor import app
from CourseEditor.courses.models import Course
from CourseEditor.usercourse.models import UserCourse
from flask import render_template
from flask_login import current_user, login_required

@app.route("/grades/grades.html") 
@login_required
def grades_show():
    return render_template("grades/grades.html", grades = Course.find_completed_courses(current_user.id))