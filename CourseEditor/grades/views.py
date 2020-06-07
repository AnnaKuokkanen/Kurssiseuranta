from CourseEditor import app
from flask import render_template
from flask_login import login_required

@app.route("/grades/grades.html") 
@login_required
def grades_show():
    return render_template("grades/grades.html")