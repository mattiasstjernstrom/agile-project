from flask import Blueprint, render_template, request
from forms import SubscribeNewsletterForm
from areas.products.services import newSubscriber

siteBluePrint = Blueprint("site", __name__)


@siteBluePrint.route("/contact")
def contact() -> str:

    form = SubscribeNewsletterForm()
    errorMessage = ""
    if request.method == "POST":
        errorMessage = newSubscriber()

    return render_template("site/contact.html", form=form, errorMessage=errorMessage)


@siteBluePrint.route("/terms")
def terms() -> str:

    form = SubscribeNewsletterForm()
    errorMessage = ""
    if request.method == "POST":
        errorMessage = newSubscriber()

    return render_template("site/terms.html", form=form, errorMessage=errorMessage)


@siteBluePrint.route("/about")
def about() -> str:

    form = SubscribeNewsletterForm()
    errorMessage = ""
    if request.method == "POST":
        errorMessage = newSubscriber()

    return render_template("site/about.html", form=form, errorMessage=errorMessage)
