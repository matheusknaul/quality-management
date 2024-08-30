from flask import Flask,redirect,url_for,render_template,request

from flask import Flask
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate

# Criação do objeto SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Supplier, Category

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)