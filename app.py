from flask import Flask

from flask_migrate import Migrate, upgrade
from flask_security import Security

from areas.site.sitePages import siteBluePrint
from areas.products import productBluePrint
from areas.admin import adminBluePrint
from areas.error import errorHandlersBluePrint
from models import db, seedData, user_datastore


app = Flask(__name__)
app.config.from_object("config.ConfigDebug")

db.app = app
db.init_app(app)
migrate = Migrate(app, db)
security = Security(app, user_datastore)
# user_manager.app = app
# user_manager.init_app(app,db,User)


app.register_blueprint(adminBluePrint, url_prefix="/admin")
app.register_blueprint(productBluePrint)
app.register_blueprint(siteBluePrint)
app.register_blueprint(errorHandlersBluePrint)


if __name__ == "__main__":
    with app.app_context():
        upgrade()
        seedData(security)
        app.run(debug=True)
