from CourseEditor import app
from CourseEditor.courses.models import Course
from flask import render_template
from flask_login import current_user, login_required

@app.route("/plans/plan.html") 
@login_required
def plans_show():
    return render_template("plans/plan.html", plans = Course.list_course_and_teacher(current_user.id))