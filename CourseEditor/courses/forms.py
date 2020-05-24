from flask_wtf import FlaskForm
from wtforms import StringField

class NewForm(FlaskForm):
    name = StringField("Nimi")
    content = StringField("Sisältö")
    time = StringField("Ajankohta")
    class Meta:
        csrf = False