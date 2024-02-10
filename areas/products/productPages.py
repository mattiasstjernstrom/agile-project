from .services import (
    getCategory,
    getTrendingCategories,
    getProduct,
    getTrendingProducts,
    newSubscriber,
)
from forms import NewsletterForm
from flask import Blueprint, render_template, request, redirect, jsonify
from forms import NewsletterForm
from .services import (
    getCategory,
    getTrendingCategories,
    getProduct,
    getTrendingProducts,
)

productBluePrint = Blueprint("product", __name__)


@productBluePrint.route("/", methods=["GET", "POST"])
def index() -> str:
    form = NewsletterForm()
    errorMessage = ""
    if request.method == "POST":
        errorMessage = newSubscriber()

    trendingCategories = []
    trendingCategories = getTrendingCategories()
    trendingProducts = getTrendingProducts()

    form = NewsletterForm(request.form)
    return render_template(
        "products/index.html",
        trendingCategories=trendingCategories,
        products=trendingProducts,
        form=form,
    )


@productBluePrint.route("/category/<id>", methods=["GET", "POST"])
def category(id) -> str:
    form = NewsletterForm()
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


@productBluePrint.route("/newsletter", methods=["GET", "POST"])
def newsletter() -> str:
    if request.method == "GET":

        return "Method Not Allowed", 405
    form = NewsletterForm(request.form)
    # TODO: Handler for user already exists, return

    #! This is a placeholder for the user check, debugging purposes only
    # Return true if the user exists
    user_exist = False

    if user_exist == True and form.validate_on_submit():

        return "Email is already subscribed to the newsletter", 409
    if form.validate_on_submit():
        # TODO: Save the email to the database

        # Logic to save the email to the database
        # ...

        # Return a success message as a JSON response to javascript
        return jsonify("Form Submitted Successfully"), 200
    return form.errors, 400


@productBluePrint.route("/category/<id>")
def category(id) -> str:
    category = getCategory(id)
    return render_template("products/category.html", category=category)


@productBluePrint.route("/product/<id>")
def product(id) -> str:
    product = getProduct(id)
    return render_template("products/product.html", product=product)
