from routes.home import home_route
from routes.norma import norma_route
from database.database import db
from database.models.norma import Norma

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(norma_route, url_prefix='/normas')

def configure_db():
    db.connect()
    db.create_tables([Norma])