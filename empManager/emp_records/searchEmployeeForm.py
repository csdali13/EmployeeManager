
from flask_wtf import FlaskForm  
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class SearchEmployeeForm(FlaskForm):
    name = StringField('Name to be searched?', validators = [DataRequired(), Length(max=200)])
    designation = StringField('Search by designation', validators = [DataRequired(), Length(max=80)])
    phone = StringField('Search by Mobile number')
    submit = SubmitField('Search Employee')
    cancel = SubmitField('Cancel')


