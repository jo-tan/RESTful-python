from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
db_name = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(20), unique=True, nullable=False)
    value = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.key} - {self.value}"

#initiate the db(run once)
with app.app_context():
    print("Creating tables...")
    db.create_all()
    print("Tables created!")

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
    return 'Hi from index!'

@app.route('/items')
def get_items():
    values = Data.query.all()

    output = []
    for row in values:
        row_data = {'id': row.id,'key': row.key, 'value': row.value}
        output.append(row_data)
    return {"Data": output}

@app.route('/items/<id>')
def get_item(id):
    row = Data.query.get_or_404(id)
    return {"id": row.id, "key": row.key, "value": row.value}
