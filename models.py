from app import db

class Supplier(db.Model):
    __tablename__ = "supplier"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = 