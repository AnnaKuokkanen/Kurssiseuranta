from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewForm(FlaskForm):
    name = StringField("Nimi")
    content = StringField("Sisältö")
    time = StringField("Ajankohta")
    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    name = StringField("Hae nimen perusteella", [validators.Length(min=2)])
    class Meta:
        csrf = False

class UpdateForm(FlaskForm):
    name = StringField("Nimi")
    content = StringField("Sisältö")
    time = StringField("Ajankohta")
    class Meta:
        csrf = False