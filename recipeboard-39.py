# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: RecipeBoard
def repair_recipes():
    for r in recipes:
        if r.name is None:
            r.name = "Unnamed Recipe"
        if r.servings <= 0:
            r.servings = 1
        if r.cost < 0:
            r.cost = 0.0
