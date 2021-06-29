from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_migrate import Migrate


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object('config.Config')

    migrate = Migrate(app, db)

    api = Api(app, prefix="/api/v1")
    db.init_app(app)

    from app.resources.buyer import Buyers
    api.add_resource(Buyers, '/buyers')

    return app