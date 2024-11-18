from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
from configuration import configure_all
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins="http://127.0.0.1:3000")

configure_all(app)

app.run(debug=True)