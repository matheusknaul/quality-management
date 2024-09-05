from routes.home import home_route
from routes.norma import norma_route
from routes.fornecedor import fornecedor_route
from routes.analise_critica import analise_critica_route
from database.database import db
from database.models.norma import Norma
from database.models.fornecedor import Fornecedor

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(norma_route, url_prefix='/normas')
    app.register_blueprint(fornecedor_route, url_prefix='/fornecedores')
    app.register_blueprint(analise_critica_route, url_prefix='/analise_critica')

def configure_db():
    db.connect()
    db.create_tables([Norma])