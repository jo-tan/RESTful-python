from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db_name = 'data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

db = SQLAlchemy()

class Data(db.Model):
    __tablename__='data'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(20), unique=True, nullable=False)
    value = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.key} - {self.value}"

@app.route('/')
def index():
    return 'Hi from index!'

@app.route('/api')
def get_api():
    return {"key": "value"}
