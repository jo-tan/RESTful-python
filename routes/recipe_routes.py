from flask import Blueprint, request, jsonify
from models.recipes import db, Recipe

recipe_bp = Blueprint('recipe_bp', __name__)

@recipe_bp.route('/', methods=['GET'])
def get_all_recipes():
    recipes = Recipe.query.all()
    return jsonify([r.to_dict() for r in recipes])

@recipe_bp.route('/', methods=['POST'])
def add_recipe():
    data = request.json
    recipe = Recipe(
        name=data['name'],
        category=data['category'],
        cooking_method=data['cooking_method'],
        ingredients=data['ingredients'],
        seasoning=data.get('seasoning'),
        cooking_time=data['cooking_time'],
        instructions=data.get('instructions')
    )
    db.session.add(recipe)
    db.session.commit()
    return jsonify(recipe.to_dict()), 201
