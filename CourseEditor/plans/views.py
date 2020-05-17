from CourseEditor import app
from flask import render_template

@app.route("/plans/plan.html") 
def plans_show():
    return render_template("plans/plan.html")