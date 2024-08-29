from flask import Flask,redirect,url_for,render_template,request

from flask import Flask
from flask_sqlalchemy import SQLAlchemy # type: ignore

# Criação do objeto SQLAlchemy
db = SQLAlchemy()

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)