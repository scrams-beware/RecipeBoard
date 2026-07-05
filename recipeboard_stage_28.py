# === Stage 28: Add overdue item detection based on due dates ===
# Project: RecipeBoard
from datetime import date, timedelta

def check_overdue_items(recipes: list[dict], today: date = None) -> dict[str, list[str]]:
    if today is None:
        today = date.today()
    
    overdue_map = {}  # recipe_name -> list of overdue ingredient names
    
    for recipe in recipes:
        name = recipe.get("name", "Unknown")
        due_date_str = recipe.get("due_date")
        
        if not due_date_str:
            continue
            
        try:
            due_date = date.fromisoformat(due_date_str)
            
            # Calculate days overdue (negative means past due)
            days_diff = (today - due_date).days
            
            if days_diff > 0:  # Overdue
                ingredients = recipe.get("ingredients", [])
                for ing in ingredients:
                    overdue_map.setdefault(name, []).append(ing["name"])
                    
        except ValueError:
            continue  # Skip invalid date formats
    
    return overdue_map
