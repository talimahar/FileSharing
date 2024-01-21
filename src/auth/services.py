# src/auth/services.py
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User
from werkzeug.security import check_password_hash


def create_user(username, password, role):
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

def get_user(username):
    return User.query.filter_by(username=username).first()

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def check_password(user, password):
    return check_password_hash(user.password, password)
