from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
from configuration import configure_all

app = Flask(__name__)

configure_all(app)

app.run(debug=True)