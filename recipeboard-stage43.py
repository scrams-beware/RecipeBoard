# === Stage 43: Add CSV import for the primary record type ===
# Project: RecipeBoard
def import_recipe_from_csv(file_path):
    """Import a recipe from a CSV file with columns: name, ingredients, servings, cost."""
    try:
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                recipe_name = row["name"].strip()
                if not recipe_name:
                    continue
                ingredients_str = row.get("ingredients", "").strip()
                servings = int(row.get("servings", 1).strip())
                cost = float(row.get("cost", 0.0))

                recipe = Recipe(name=recipe_name, servings=servings, cost=cost)
                if ingredients_str:
                    for ingredient in ingredients_str.split(";"):
                        ing = ingredient.strip()
                        if ing:
                            recipe.add_ingredient(ing)
                board.append_recipe(recipe)
        print(f"Imported {board.count_recipes()} recipe(s) from '{file_path}'.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
