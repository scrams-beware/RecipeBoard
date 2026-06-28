# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: RecipeBoard
def sort_recipes(recipes, key="title", reverse=False):
    if key == "date":
        return sorted(recipes, key=lambda r: r.get("created_at", 0), reverse=reverse)
    elif key == "priority":
        return sorted(recipes, key=lambda r: r.get("priority", 0), reverse=True)
    elif key == "last_update":
        return sorted(recipes, key=lambda r: r.get("updated_at", 0), reverse=False)
    else:
        return sorted(recipes, key=lambda r: str(r.get(key, "")).lower(), reverse=reverse)
