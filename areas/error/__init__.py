from flask import Blueprint, render_template
from werkzeug.exceptions import HTTPException


errorHandlersBluePrint = Blueprint("errorHandlers", __name__)


@errorHandlersBluePrint.app_errorhandler(HTTPException)
def handle_exception(e):
    return render_template("error/_error_template.html", error=e), e.code
