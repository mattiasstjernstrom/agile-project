from flask import Blueprint, render_template, redirect, request
from forms import NewsletterForm
from areas.products.services import newSubscriber

siteBluePrint = Blueprint('site', __name__)

@siteBluePrint.route('/contact')
def contact() -> str:
     form=NewsletterForm()
     errorMessage = ""
     if request.method == 'POST':
          errorMessage = newSubscriber()

     return render_template('site/contact.html', form=form, errorMessage=errorMessage)

@siteBluePrint.route('/terms')
def terms() -> str:
     form=NewsletterForm()
     errorMessage = ""
     if request.method == 'POST':
          errorMessage = newSubscriber()

     return render_template('site/terms.html', form=form, errorMessage=errorMessage)

@siteBluePrint.route('/about')
def about() -> str:
     form=NewsletterForm()
     errorMessage = ""
     if request.method == 'POST':
          errorMessage = newSubscriber()

     return render_template('site/about.html', form=form, errorMessage=errorMessage)
