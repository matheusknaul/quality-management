from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')

@home_route.route('/nota_fiscal')
def nota_fisca():
    return render_template('home/nota_fiscal')

@home_route.route('/solicitar_aprovacao')
def solicitar_aprovacao():
    return render_template('home/solicitar_aprovacao')