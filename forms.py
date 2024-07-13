from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp


class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email address.")])
    phone = StringField('Phone', validators=[DataRequired(), Regexp(regex=r'^\+?1?\d{9,15}$', message="Invalid phone "
                                                                                                      "number.")])
    submit = SubmitField('Add User')

