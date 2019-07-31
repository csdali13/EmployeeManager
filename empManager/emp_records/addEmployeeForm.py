
from flask_wtf import FlaskForm  
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class AddEmployeeForm(FlaskForm):
    name = StringField('Whats your name?', validators = [DataRequired(), Length(max=200)])
    designation = StringField('Enter your designation', validators = [DataRequired(), Length(max=80)])
    address = StringField('Your contact address', validators = [DataRequired(), Length(max=400)])
    phone = StringField('Mobile number')
    department_id = StringField('Enter the department #', validators = [DataRequired()])
    submit = SubmitField('Add Employee')
    cancel = SubmitField('Cancel')


