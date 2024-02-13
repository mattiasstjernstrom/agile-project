from flask_wtf import FlaskForm
from wtforms import EmailField, IntegerField, StringField, TextAreaField, BooleanField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired, Email, Length


class SubscribeNewsletterForm(FlaskForm):
    newsletter_email = EmailField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Invalid Email Format"),
            Length(min=7, message="Email must be at least %(min)d characters long"),
        ],
    )


class DeleteNewsletterEmailForm(FlaskForm):
    email_id = IntegerField("email_id", [DataRequired()], widget=HiddenInput())


class WriteNewsletterForm(FlaskForm):
    subject = StringField(
        "Subject", validators=[DataRequired(message="Subject is required")]
    )
    content = TextAreaField(
        "Content", validators=[DataRequired(message="Content is required")]
    )
