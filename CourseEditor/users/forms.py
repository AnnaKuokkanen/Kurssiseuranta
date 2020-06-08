from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class LoginForm(FlaskForm):

    username = StringField("Käyttäjänimi", [validators.Length(min=8, max=144)])
    password = PasswordField("Salasana", [validators.Length(min=8, max=144)])

    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):

    firstname = StringField("Nimi", [validators.Length(min=2, max=144)])
    lastname = StringField("Sukunimi", [validators.Length(min=2, max=144)])
    username = StringField("Käyttäjänimi", [validators.Length(min=8, max=144)])
    password = PasswordField("Salasana", [validators.Length(min=8, max=144)])
    
    class Meta:
        csrf = False

class UpdateForm(FlaskForm):

    firstname = StringField("Nimi", [validators.Length(min=2, max=144)])
    lastname = StringField("Sukunimi", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False