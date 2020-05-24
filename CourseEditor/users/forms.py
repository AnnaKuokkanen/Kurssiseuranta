from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField

class LoginForm(FlaskForm):

    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")

    class Meta:
        csrf = False