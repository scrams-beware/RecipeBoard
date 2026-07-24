# === Stage 73: Add a lightweight HTML report export ===
# Project: RecipeBoard
def export_html_report(recipe_board, output_path="report.html"):
    """Export a lightweight HTML report of the recipe board."""
    html = "<!DOCTYPE html><html><head><meta charset='utf-8'>"
    html += "<title>RecipeBoard Report</title></head><body>"
    html += "<h1>Recipe Board Summary</h1>"
    html += f"<p>Total Recipes: {len(recipe_board.recipes)}</p>"
    for recipe in recipe_board.recipes:
        ingredients = recipe.ingredients if hasattr(recipe, 'ingredients') else []
        total_cost = sum(ing['cost'] for ing in ingredients) if ingredients else 0
        html += f"<h2>{recipe.name}</h2>"
        html += f"<p>Ingredients ({len(ingredients)}):</p><ul>"
        for ing in ingredients:
            html += f"<li>{ing.get('name', 'Unknown')}: {ing.get('quantity', 0)} @ ${ing.get('cost', 0)}</li>"
        html += "</ul><p>Total Cost: $%.2f</p>" % total_cost
    html += "</body></html>"
    with open(output_path, "w") as f:
        f.write(html)
