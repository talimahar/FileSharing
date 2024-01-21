# src/auth/controllers.py
from flask import Blueprint, request, jsonify
from .services import *

auth_blueprint = Blueprint('auth', __name__)


def create_access_token(identity):
    return "generated_token"


@auth_blueprint.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data['username']
    password = data['password']
    user = get_user(username)

    if user and check_password(user, password):
        access_token = create_access_token(identity=username)
        return {"access_token": access_token}, 200
    else:
        return {"message": "Invalid credentials"}, 401


@auth_blueprint.route('/auth/logout', methods=['POST'])
def logout():
    data = request.get_json()
    access_token = data['generated_token']
    return {"message": "Logout Successful"}, 401