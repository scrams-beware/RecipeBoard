# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: RecipeBoard
import json, os

def load_recipe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict) and 'name' in data and 'ingredients' in data:
            return data
    except (json.JSONDecodeError, FileNotFoundError, KeyError):
        print(f"Warning: Skipping malformed or missing file {path}")
    return None

def load_all_recipes(folder="recipes"):
    recipes = []
    if not os.path.isdir(folder):
        return recipes
    for filename in sorted(os.listdir(folder)):
        if filename.endswith('.json'):
            recipe = load_recipe(os.path.join(folder, filename))
            if recipe:
                recipes.append(recipe)
    return recipes
