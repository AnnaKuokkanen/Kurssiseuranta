from CourseEditor import app
from CourseEditor.courses.models import Course
from CourseEditor.usercourse.models import UserCourse
from flask import render_template
from flask_login import current_user, login_required

@app.route("/plans/plan.html") 
@login_required
def plans_show():
    #return render_template("plans/plan.html", plans = Course.find_planned_courses(current_user.id))
    return render_template("plans/plan.html", plans = Course.query.all())