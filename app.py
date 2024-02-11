from flask import Flask, render_template, request, redirect  # importerat även dessa: render_template, request, redirect
from models import db, seedData, NewsletterEmails # importerar även NewsletterEmails från models
from flask_migrate import Migrate, upgrade
from areas.site.sitePages import siteBluePrint
from areas.products.productPages import productBluePrint
from flask_security import roles_accepted, auth_required, logout_user

app = Flask(__name__)
app.config.from_object("config.ConfigDebug")

db.app = app
db.init_app(app)
migrate = Migrate(app, db)
# user_manager.app = app
# user_manager.init_app(app,db,User)

@app.route('/admin') # Tar med mig NewsletterEmails till admin page
def admin():
    return render_template("admin.html", values=NewsletterEmails.query.all())

@app.route('/delete', methods=['POST'])  ## Skickar till denna sida som söker fram emailen i databasen
def delete_email():
    email_id = int(request.form['email_id'])
    email_to_delete = NewsletterEmails.query.get(email_id)
    if email_to_delete:
        db.session.delete(email_to_delete)
        db.session.commit()
        return redirect('/admin')  # Skickar tillbaka till adminsidan efter, raderingen
    else:
        return "Email not found", 404

app.register_blueprint(siteBluePrint)
app.register_blueprint(productBluePrint)

if __name__ == "__main__":
    with app.app_context():
        upgrade()
        seedData(app)
        app.run(debug=True)
