from flask import Blueprint, render_template, request
from werkzeug.security import generate_password_hash
from database.models.user import User, Funcao

authentication_route = Blueprint('analise_critica', __name__)

@authentication_route.route('/register', methods=["POST", "GET"])
def create_user(username, password):
    gen_password_hash = generate_password_hash(password)
    user = User.create(username=username, password_hash = gen_password_hash)

@authentication_route.route('/login', methods=["POST", "GET"])
def login():
    pass