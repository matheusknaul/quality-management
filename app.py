from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from routes.home import home_route
from routes.norma import norma_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(norma_route, url_prefix='/normas')

app.run(debug=True)