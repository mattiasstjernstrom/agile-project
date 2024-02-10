from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, Form
from wtforms.validators import InputRequired, Email

class NewsletterForm(FlaskForm):
    email = StringField(label='Email', id='email', name='email', 
                        validators=[InputRequired(), Email()])

