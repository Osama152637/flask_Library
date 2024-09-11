from flask import Blueprint

bookBlueprint = Blueprint("books", __name__, url_prefix="/books")

from app.book import views