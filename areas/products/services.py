from models import db, Category, Product, NewsletterEmails
from forms import NewsletterForm

def getTrendingCategories():
    return Category.query.order_by(Category.CategoryID.desc()).paginate(page=1,per_page=4,error_out=False).items

def getCategory(id):
    return Category.query.filter(Category.CategoryID ==id).first()

def getProduct(id):
    return Product.query.filter(Product.ProductID ==id).first()

def getTrendingProducts():
    return Product.query.order_by(Product.ProductID.desc()).paginate(page=1,per_page=8,error_out=False).items


def newSubscriber():
    form = NewsletterForm()
    errorMessage = ""
    if form.validate():
        if NewsletterEmails.query.filter_by(Email = form.email.data).first() == None:
            new_sub = NewsletterEmails(Email = form.email.data)
            db.session.add(new_sub)
            db.session.commit()
            return errorMessage
        else:
            errorMessage = 'Email finns redan'
            return errorMessage
    else:
        errorMessage = 'Emailfältet tomt!'
        return errorMessage