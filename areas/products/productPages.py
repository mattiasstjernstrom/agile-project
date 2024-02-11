from .services import (
    getCategory,
    getTrendingCategories,
    getProduct,
    getTrendingProducts,
    newSubscriber,
)
from forms import NewsletterForm
from flask import Blueprint, render_template, request
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


@productBluePrint.route("/newsletter", methods=["GET", "POST"])
def newsletter() -> str:
    if request.method == "GET":

        return "Method Not Allowed", 405
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
