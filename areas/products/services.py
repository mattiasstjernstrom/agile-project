from models import Category, Product

def getTrendingCategories():
    return Category.query.order_by(Category.CategoryID.desc()).paginate(page=1,per_page=4,error_out=False).items

def getCategory(id):
    return Category.query.filter(Category.CategoryID ==id).first()

def getProduct(id):
    return Product.query.filter(Product.ProductID ==id).first()

def getTrendingProducts():
    return Product.query.order_by(Product.ProductID.desc()).paginate(page=1,per_page=8,error_out=False).items
