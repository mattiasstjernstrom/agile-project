import datetime as dt

from flask import Blueprint, render_template, request, redirect
from flask_security import roles_accepted

from forms import DeleteNewsletterEmailForm, WriteNewsletterForm
from models import NewsletterEmails, Newsletter, db
from extensions import mail  # Förbreedd för att kunna skicka mail

my_blueprint = Blueprint("my_blueprint", __name__)

adminBluePrint = Blueprint("admin", __name__)


@adminBluePrint.route("/")
@roles_accepted("Admin", "Staff")
def admin():
    return render_template("admin/admin.html", values=NewsletterEmails.query.all())


@adminBluePrint.route("/manage-newsletter", methods=["GET", "POST"])
@roles_accepted("Admin", "Staff")
def manage_newsletter():
    form_delete = DeleteNewsletterEmailForm(request.form)
    return render_template(
        "admin/manageNewsletter.html",
        values=NewsletterEmails.query.all(),
        form_delete=form_delete,
    )


@adminBluePrint.route("/write-newsletter", methods=["GET", "POST"])
@roles_accepted("Admin", "Staff")
def write_newsletter():
    write_newsletter = WriteNewsletterForm(request.form)
    if write_newsletter.validate():
        subject = write_newsletter.subject.data
        content = write_newsletter.content.data
        date = dt.datetime.now()
        sent = False
        newsletter = Newsletter(Subject=subject, Content=content, Date=date, Sent=sent)
        db.session.add(newsletter)
        db.session.commit()
        return redirect("/admin/manage-newsletter")
    return render_template(
        "admin/writeNewsletter.html", write_newsletter=write_newsletter
    )


@adminBluePrint.route("/delete-email", methods=["POST"])
@roles_accepted("Admin", "Staff")
def delete_email():
    if request.method == "POST":
        form_delete = DeleteNewsletterEmailForm(request.form)
        if form_delete.validate():
            email_id = form_delete.email_id.data
            email_to_delete = NewsletterEmails.query.get(email_id)
            if email_to_delete:
                db.session.delete(email_to_delete)
                db.session.commit()
                return redirect("/admin/manage-newsletter")
        else:
            return "Email not found", 404
    else:
        return "Invalid form data", 400
