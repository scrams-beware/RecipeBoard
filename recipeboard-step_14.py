# === Stage 14: Add file load support with fallback demo data ===
# Project: RecipeBoard
def load_recipe_data(source=None):
    if source:
        try:
            import json
            with open(source, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    demo = {
        "recipes": [
            {"id": 1, "name": "Pasta", "ingredients": [{"item": "Flour", "qty": 200}, {"item": "Eggs", "qty": 3}], "cost_per_ingredient": [1.5, 2.0], "yield_portions": 4}
        ],
        "menu_plan": []
    }
    return demo
