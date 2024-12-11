from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
from config_blueprints import configure_all
from flask_cors import CORS
import config


app = Flask(__name__)

app.config.from_object(config)

CORS(app, resources={r"/*": {"origins": app.config['CORS_ORIGINS']}})

configure_all(app)

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])
