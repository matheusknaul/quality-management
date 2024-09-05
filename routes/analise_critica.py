from flask import Blueprint, render_template, request

analise_critica_route = Blueprint('analise_critica', __name__)

@analise_critica_route.route('/')
def index():
    return render_template('analise_critica/index.html')