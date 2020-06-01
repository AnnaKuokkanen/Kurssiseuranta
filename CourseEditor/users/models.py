from CourseEditor import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(144), nullable=False)
    lastname = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    courses = db.relationship('Course', secondary='account_course', backref='account', lazy=True)

    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

    def get_id(self):
        return self.id
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def remove_row(user_id, course_id):
        stmt = text("DELETE FROM account_course WHERE user_id = :user AND course_id = :course").params(user=user_id, course=course_id)
        db.engine.execute(stmt)