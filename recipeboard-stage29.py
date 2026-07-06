# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: RecipeBoard
def upcoming_items(recipes, days_ahead=7):
    """Return a list of (recipe_name, day_offset) for recipes due within `days_ahead` days."""
    from datetime import date, timedelta
    today = date.today()
    result = []
    for r in recipes:
        if not hasattr(r, 'next_prep') or not hasattr(r, 'prep_date'):
            continue
        prep = getattr(r, 'prep_date', None)
        if prep and prep <= today + timedelta(days=days_ahead):
            offset = (prep - today).days
            result.append((r.name, offset))
    return sorted(result, key=lambda x: x[1])

def next_expiring_ingredients(ingredients, days_ahead=7):
    """Return a list of (ingredient_name, day_offset) for ingredients expiring soon."""
    from datetime import date, timedelta
    today = date.today()
    result = []
    for ing in ingredients:
        if not hasattr(ing, 'expiry_date'):
            continue
        expiry = getattr(ing, 'expiry_date', None)
        if expiry and expiry <= today + timedelta(days=days_ahead):
            offset = (expiry - today).days
            result.append((ing.name, offset))
    return sorted(result, key=lambda x: x[1])

def upcoming_shopping_items(shopping_lists, days_ahead=7):
    """Return a list of (list_name, item_name) for items in active shopping lists due soon."""
    from datetime import date, timedelta
    today = date.today()
    result = []
    for sl in shopping_lists:
        if not hasattr(sl, 'deadline') or not hasattr(sl, 'items'):
            continue
        deadline = getattr(sl, 'deadline', None)
        items = getattr(sl, 'items', [])
        if deadline and deadline <= today + timedelta(days=days_ahead):
            for item in items:
                result.append((sl.name, item))
    return sorted(result, key=lambda x: (x[1] == 'pending'))

def display_reminders():
    """Show all upcoming reminders grouped by type."""
    print("\n=== Upcoming Reminders ===")
    print("Recipes:")
    for name, day in upcoming_items([], 7):
        print(f"  - {name} (in {day} days)")
    print("Ingredients:")
    for name, day in next_expiring_ingredients([], 7):
        print(f"  - {name} expires in {day} days")
    print("Shopping Lists:")
    for list_name, item in upcoming_shopping_items([], 7):
        print(f"  - {list_name}: {item}")

display_reminders()
