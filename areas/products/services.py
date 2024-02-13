from flask import jsonify
from models import db, Category, Product, NewsletterEmails


def getTrendingCategories():
    return (
        Category.query.order_by(Category.CategoryID.desc())
        .paginate(page=1, per_page=3, error_out=False)
        .items
    )


def getCategory(id):
    return Category.query.filter(Category.CategoryID == id).first()


def getProduct(id):
    return Product.query.filter(Product.ProductID == id).first()


def getTrendingProducts():
    return (
        Product.query.order_by(Product.ProductID.desc())
        .paginate(page=1, per_page=9, error_out=False)
        .items
    )


def newSubscriber(form):
    if form.validate():
        if user_is_subscribed(form.newsletter_email.data):
            return "Email is already subscribed to the newsletter", 409
        else:
            new_sub = NewsletterEmails(Email=form.newsletter_email.data)
            db.session.add(new_sub)
            db.session.commit()
            return jsonify("Form Submitted Successfully"), 200
    else:
        return form.errors, 400


def user_is_subscribed(email):
    return NewsletterEmails.query.filter_by(Email=email).first() is not None
