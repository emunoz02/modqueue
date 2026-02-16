from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    # Getting JSON from client
    data = request.get_json()
    
    # Extracting data from response
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    
    # Making sure all fields have been answered
    if not all([username, email, password, first_name, last_name]):
        return jsonify({'error': 'All fields are required'}), 400
    
    # Check if username or email already exists
    existing_user = User.query.filter(
        (User.username == username) | (User.email == email)
    ).first()
    
    if existing_user:
        return jsonify({'error': 'Username or email already exists. Try logging in!'}), 409
    
    hashed_password = generate_password_hash(password)
    
    new_user = User(
        username=username,
        password_hash=hashed_password,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create user', 'details': str(e)}), 500
    
    return jsonify({
        'message': 'User created successfully',
        'user': {
            'id': new_user.id,
            'username': new_user.username,
            'email': new_user.email,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name
        }
    }
    ), 201
    
@auth_bp.route('/login', methods=["POST"])
def login():
    # Get JSON data from request
    data = request.get_json()

    # Extract email and password
    email = data.get('email')
    password = data.get('password')

    # Validate both fields are present
    if not all([email, password]):
        return jsonify({'error': 'All fields are required.'}), 400

    # Find user by email
    user = User.query.filter(User.email == email).first()

    # Check if user exists
    if not user:
        return jsonify({'error': 'User does not exist.'}), 401

    # Verify password matches hash
    if not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Incorrect password. Try again.'}), 401

    # Create JWT token with 24-hour expiration
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=24)

    token = jwt.encode({
        'user_id': user.id,
        'exp': expiration
    },
        os.getenv('SECRET_KEY'),
        algorithm='HS256'
    )

    # Return token and success message
    return jsonify({
        'token': token,
        'message': 'Login successful'
    }), 200