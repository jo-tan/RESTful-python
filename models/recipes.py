from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    category = db.Column(db.String(50), nullable=False)  # e.g. "meal", "soup"
    cooking_method = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.JSON, nullable=False)
    seasoning = db.Column(db.JSON, nullable=True)
    cooking_time = db.Column(db.Integer, nullable=False)  # in minutes
    instructions = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def get_recipeDetail(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "cooking_method": self.cooking_method,
            "ingredients": self.ingredients,
            "seasoning": self.seasoning,
            "cooking_time": self.cooking_time,
            "instructions": self.instructions,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    def __repr__(self):
        return f"{self.key} - {self.value}"