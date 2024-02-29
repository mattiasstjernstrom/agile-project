from flask import Flask

from flask_migrate import Migrate, upgrade
from flask_login import current_user
from flask_mail import Mail
from flask_security import Security


from areas.site.sitePages import siteBluePrint
from areas.products import productBluePrint
from areas.admin import adminBluePrint
from areas.error import errorHandlersBluePrint
from areas.products.services import user_is_subscribed, getTrendingCategories
from models import db, seedData, user_datastore, Category

app = Flask(__name__)
app.config.from_object("config.ConfigDebug")

mail = Mail(app)
db.app = app
db.init_app(app)
migrate = Migrate(app, db)
security = Security(app, user_datastore)

mail.init_app(app)
# user_manager.app = app
# user_manager.init_app(app,db,User)


app.register_blueprint(adminBluePrint, url_prefix="/admin")
app.register_blueprint(productBluePrint)
app.register_blueprint(siteBluePrint)
app.register_blueprint(errorHandlersBluePrint)


#! If you need something to be available in all templates, you can use this context processor.
@app.context_processor
def context_processor():
    is_subscribed_to_newsletter = False
    if current_user.is_authenticated and user_is_subscribed(current_user.email):
        is_subscribed_to_newsletter = True

    all_categories = Category().query.all()
    top_categories = getTrendingCategories(5)

    # TODO: Replace with actual data:
    user_specific_context = {
        "cart_count": 1,
        "wishlist_count": 1,
    }

    return dict(
        is_subscribed_to_newsletter=is_subscribed_to_newsletter,
        all_categories=all_categories,
        top_categories=top_categories,
        **user_specific_context
    )


if __name__ == "__main__":
    with app.app_context():
        # upgrade()
        seedData(security)
        app.run(debug=True, port=5000)
