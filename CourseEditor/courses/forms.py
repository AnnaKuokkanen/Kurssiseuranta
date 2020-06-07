from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class SearchForm(FlaskForm):
    name = StringField("Hae nimen perusteella", [validators.Length(min=2, max=144)])
    class Meta:
        csrf = False

class CourseForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=2, max=144)])
    content = StringField("Sisältö", [validators.Length(min=2, max=144)])
    time = StringField("Ajankohta", [validators.Length(min=2, max=144)])
    teacher_firstname = StringField("Opettajan etunimi", [validators.Length(min=2, max=144)])
    teacher_lastname = StringField("Opettajan sukunimi", [validators.Length(min=2, max=144)])
    completed = BooleanField("Suoritettu")
    planned = BooleanField("Suunniteltu")
    class Meta:
        csrf = False