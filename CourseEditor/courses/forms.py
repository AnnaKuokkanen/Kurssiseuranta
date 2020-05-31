from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=144)])
    content = StringField("Sisältö", [validators.Length(min=2, max=144)])
    time = StringField("Ajankohta", [validators.Length(min=2, max=144)])
    teacher_firstname = StringField("Opettajan etunimi", [validators.Length(min=2, max=144)])
    teacher_lastname = StringField("Opettajan sukunimi", [validators.Length(min=2, max=144)])
    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    name = StringField("Hae nimen perusteella", [validators.Length(min=2, max=144)])
    class Meta:
        csrf = False

class UpdateForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=144)])
    content = StringField("Sisältö", [validators.Length(min=2, max=144)])
    time = StringField("Ajankohta", [validators.Length(min=2, max=144)])
    teacher_firstname = StringField("Opettajan etunimi", [validators.Length(min=2, max=144)])
    teacher_lastname = StringField("Opettajan sukunimi", [validators.Length(min=2, max=144)])
    class Meta:
        csrf = False