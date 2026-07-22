# === Stage 67: Add a function that returns key project metrics ===
# Project: RecipeBoard
def project_metrics(recipes, shopping_lists):
    """Return key metrics for the RecipeBoard project."""
    total_ingredients = sum(len(r.get("ingredients", [])) for r in recipes)
    unique_shopping_items = set()
    for sl in shopping_lists:
        if isinstance(sl, dict):
            unique_shopping_items.update(sl.get("items", []))
        elif isinstance(sl, list):
            unique_shopping_items.update(sl)

    return {
        "total_recipes": len(recipes),
        "total_ingredients_used": total_ingredients,
        "unique_shopping_items": len(unique_shopping_items),
        "shopping_list_count": len(shopping_lists),
    }
