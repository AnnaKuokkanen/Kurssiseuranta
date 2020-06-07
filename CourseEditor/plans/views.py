from CourseEditor import app
from flask import render_template
from flask_login import login_required

@app.route("/plans/plan.html") 
@login_required
def plans_show():
    return render_template("plans/plan.html")