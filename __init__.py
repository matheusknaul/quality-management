app = Flask(__name__)

from quality-management.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app import routes, models
