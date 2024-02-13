from flask import Blueprint, render_template, request, redirect
from forms import SubscribeNewsletterForm
from .services import (
    getCategory,
    getTrendingCategories,
    getProduct,
    getTrendingProducts,
    newSubscriber,
)

productBluePrint = Blueprint("product", __name__)


@productBluePrint.route("/", methods=["GET", "POST"])
def index() -> str:
    trendingCategories = []
    trendingCategories = getTrendingCategories()
    trendingProducts = getTrendingProducts()

    if request.method == "POST":
        newsletter_form = SubscribeNewsletterForm(request.form)
        if newsletter_form.validate_on_submit():
            pass
    else:
        newsletter_form = SubscribeNewsletterForm()
    print(newsletter_form.__dict__)
    return render_template(
        "products/index.html",
        trendingCategories=trendingCategories,
        products=trendingProducts,
        newsletter_form=newsletter_form,
    )


@productBluePrint.route("/category/<id>", methods=["GET", "POST"])
def category(id) -> str:

    form = NewsletterForm(request.form)
    errorMessage = ""
    if request.method == "POST":
        errorMessage = newSubscriber()

    category = getCategory(id)
    return render_template(
        "products/category.html",
        category=category,
        errorMessage=errorMessage,
        form=form,
    )


@productBluePrint.route("/newsletter", methods=["GET", "POST"])
def newsletter() -> str:
    if request.method == "GET":
        return render_template("newsletter/index.html")
    form = NewsletterForm(request.form)
    return newSubscriber(form)


@productBluePrint.route("/product/<id>", methods=["GET", "POST"])
def product(id) -> str:
    form = NewsletterForm()
    errorMessage = ""
    if request.method == "POST":
        errorMessage = newSubscriber()

    product = getProduct(id)
    return render_template(
        "products/product.html", product=product, errorMessage=errorMessage, form=form
    )
