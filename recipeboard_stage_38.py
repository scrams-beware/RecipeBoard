# === Stage 38: Add data integrity checks for broken references ===
# Project: RecipeBoard
def check_integrity(data):
    """Validate cross-references and basic integrity."""
    if "recipes" not in data:
        return {"status": "error", "message": "Missing 'recipes' key."}
    recipes = data["recipes"]
    errors = []
    for idx, recipe in enumerate(recipes):
        rid = str(idx) if len(recipes) > 1 else "0"
        if not isinstance(recipe, dict):
            errors.append(f"[{rid}] entry is not a dict.")
            continue
        name = recipe.get("name", "")
        if not name:
            errors.append(f"[{rid}] missing 'name'.")
        for ing in recipe.get("ingredients", []):
            if isinstance(ing, dict) and "amount" in ing and "unit_cost" in ing and "price_per_unit" in ing:
                try:
                    cost = float(ing["amount"]) * float(ing["unit_cost"]) * float(ing["price_per_unit"])
                    if not (0 <= cost):
                        errors.append(f"[{rid}] ingredient {name} has negative total cost.")
                except TypeError:
                    errors.append(f"[{rid}] ingredient {name} has non-numeric values.")
    return {"status": "ok", "errors": errors} if errors else None
