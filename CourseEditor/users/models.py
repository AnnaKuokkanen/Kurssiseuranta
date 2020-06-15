from CourseEditor import db
from CourseEditor.models import Base
from CourseEditor.usercourse.models import UserCourse
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='cascade'), nullable=False)

    courses = db.relationship('Course', secondary='account_course', cascade='all, delete-orphan', backref='account', single_parent=True, lazy=True)

    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.role_id = 1

    def get_id(self):
        return self.id
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return Role.search_role(self.role_id)

    @staticmethod
    def remove_row(user_id, course_id):
        stmt = text("DELETE FROM account_course WHERE user_id = :user AND course_id = :course").params(user=user_id, course=course_id)
        db.engine.execute(stmt)
    
    @staticmethod
    def remove_user(user_id):
        stmt = text("DELETE FROM account_course WHERE user_id = :user").params(user=user_id)
        db.engine.execute(stmt)
    

class Role(db.Model):

    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(5), nullable=False)

    users = db.relationship("User", cascade='all, delete-orphan', backref='role', single_parent=True, lazy=True)

    @staticmethod
    def search_role(role_id):
        stmt = text("SELECT Role.role FROM Role WHERE Role.id = :role").params(role=role_id)  
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"role":row[0]})
        
        return response
    