from flask_wtf import FlaskForm
from wtforms import EmailField, IntegerField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired, Email, Length


class NewsletterForm(FlaskForm):
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
