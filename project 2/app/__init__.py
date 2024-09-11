from flask import Flask
from flask_migrate import Migrate
from app.models import db
from app.config import config_options

def create_app(config_name="prd"):
    app = Flask(__name__)

    current_config = config_options[config_name]
    app.config.from_object(current_config)
    app.config.SQLALCHEMY_DATABASE_URI = current_config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)
    migrate = Migrate(app, db)

    from app.book import bookBlueprint
    app.register_blueprint(bookBlueprint)

    return app
