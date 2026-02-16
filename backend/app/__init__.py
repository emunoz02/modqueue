from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Initialize extensions (but don't attach to app yet)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """Application factory function"""

    # Create Flask app instance
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object('app.config.Config')

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models (so Flask-Migrate can detect them)
    from app import models
    from app.routes import auth_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    

    return app