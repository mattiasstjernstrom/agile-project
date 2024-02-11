from flask import Blueprint, render_template, request
from flask_security import roles_accepted
from flask import (
    render_template,
    request,
    redirect,
)
from models import NewsletterEmails, db

adminBluePrint = Blueprint("admin", __name__)


@adminBluePrint.route("/")
@roles_accepted("Admin", "Staff")
def admin():
    return render_template("admin.html", values=NewsletterEmails.query.all())


@adminBluePrint.post("/delete-email")
@roles_accepted("Admin", "Staff")
def delete_email():
    email_id = int(request.form["email_id"])
    email_to_delete = NewsletterEmails.query.get(email_id)
    if email_to_delete:
        db.session.delete(email_to_delete)
        db.session.commit()
        return redirect("/admin")
    else:
        return "Email not found", 404