from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class NewsletterForm(FlaskForm):
    newsletter_email = EmailField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Invalid Email Format"),
            Length(min=7, message="Email must be at least %(min)d characters long"),
        ],
    )


class UserForms(FlaskForm):
    email = EmailField(
        "Email",
        validators=[
            DataRequired(message="Email is required"),
            Email(message="Invalid Email Format"),
            Length(min=6, message="Email must be at least %(min)d characters long"),
        ],
    )
    password = StringField("Password", validators=[DataRequired()])
    confirm_password = StringField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    remember_me = BooleanField("Remember Me")