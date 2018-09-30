import logging

from flask import Flask

from app.settings import Config
from sqlalchemy import create_engine, orm


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return app


app = create_app()

db_engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = orm.sessionmaker(bind=db_engine)
from app.views.index import index_bp

app.register_blueprint(index_bp)

from app.models import *
