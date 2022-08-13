from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
# from flask_bootstrap import Bootstrap


app = Flask(__name__)
db = SQLAlchemy(app)
db_uri = os.environ.get('DATABASE_URL') or "postgresql://localhost/blog"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri



class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# bootstrap = Bootstrap(app)



@app.route('/')
def index():
  return render_template('index.html')
