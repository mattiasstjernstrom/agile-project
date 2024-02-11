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
    return render_template("admin/admin.html", values=NewsletterEmails.query.all())


@adminBluePrint.route("/manage-newsletter", methods=["GET", "POST"])
@roles_accepted("Admin", "Staff")
def manage_newsletter():
    return render_template(
        "admin/manageNewsletter.html", values=NewsletterEmails.query.all()
    )


@adminBluePrint.route("/write-newsletter", methods=["GET", "POST"])
@roles_accepted("Admin", "Staff")
def write_newsletter():
    return render_template("admin/writeNewsletter.html")


@adminBluePrint.post("/delete-email")
@roles_accepted("Admin", "Staff")
def delete_email():
    email_id = int(request.form["email_id"])
    email_to_delete = NewsletterEmails.query.get(email_id)
    if email_to_delete:
        db.session.delete(email_to_delete)
        db.session.commit()
        return redirect("/admin/manage-newsletter")
    else:
        return "Email not found", 404
