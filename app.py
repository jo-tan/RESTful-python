from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv

from models.recipes import db
from routes.recipe_routes import recipe_bp

load_dotenv(dotenv_path="instance/.env")
migrate = Migrate()

def setup_logging(app):
    if not os.path.exists('logs'):
        os.makedirs('logs')

    if app.logger.handlers:
        return

    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=3)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )
    file_handler.setFormatter(formatter)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('📋 Flask app started and logging is initialized.')

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///instance/recipes.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(recipe_bp, url_prefix='/api/recipes')

    setup_logging(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


