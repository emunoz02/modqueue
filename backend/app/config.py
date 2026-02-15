# This file will read the database connection string from environment variables
# Provide configuration settings for Flask and SQLAlchemy
# Keep our code clean and organized

import os

class Config:
    
    # Secret key for flask sessions (used for security)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database connection string
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://modqueue_user:pgemunoz@localhost:5432/modqueue_dev'
    
    # Disable Flask-SQLAlchemy event system (saves resources)
    SQLALCHEMY_TRACK_MODIFICATIONS = False