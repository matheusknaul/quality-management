from app import db

class Supplier(db.Model): #Fornecedores
    __tablename__ = "supplier"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.Sring(14), unique=True, nullable=False)
    address = db.Column(db.Text, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', back_populates='suppliers')

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    suppliers = db.relationship('Supplier', back_populates='category')