from CourseEditor import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(144), nullable=False)
    pin = db.Column(db.String(144), nullable=False)
    fname = db.Column(db.String(144), nullable=False)
    lname = db.Column(db.String(144), nullable=False)

    def __init__(self, user, pin, fname, lname):
        self.fname = fname
        self.lname = lname
        self.user = user
        self.pin = pin