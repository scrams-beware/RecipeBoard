# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: RecipeBoard
def validate_recipe_id(recipe_id):
    if not recipe_id:
        raise ValueError("Recipe ID cannot be empty")
    if len(recipe_id) > 10:
        raise ValueError("Recipe ID must be less than or equal to 10 characters")
    return True

def validate_ingredient_name(name):
    if not name.strip():
        raise ValueError("Ingredient name cannot be empty")
    if len(name) < 2:
        raise ValueError("Ingredient name must be at least 2 characters long")
    return name.strip()

def validate_quantity(quantity, unit="g"):
    try:
        num = float(quantity)
        if num <= 0:
            raise ValueError(f"Quantity for {unit} must be positive")
        return num
    except (ValueError, TypeError):
        raise ValueError("Invalid quantity format. Use a number.")

def validate_cost(cost):
    try:
        c = float(cost)
        if c < 0:
            raise ValueError("Cost cannot be negative")
        return round(c, 2)
    except (ValueError, TypeError):
        raise ValueError("Invalid cost format. Use a number.")

def validate_portions(portions):
    try:
        p = int(portions)
        if p <= 0:
            raise ValueError("Portions must be at least 1")
        return p
    except (ValueError, TypeError):
        raise ValueError("Invalid portions format. Use an integer.")

def validate_shopping_item(item_name, quantity, cost_per_unit):
    name = validate_ingredient_name(item_name)
    qty = validate_quantity(quantity)
    unit_cost = validate_cost(cost_per_unit)
    total = round(qty * unit_cost, 2)
    return {"name": name, "quantity": qty, "unit_cost": unit_cost, "total": total}

def validate_menu_item(recipe_id, portions):
    rid = str(recipe_id).strip()
    if not rid:
        raise ValueError("Menu item recipe ID cannot be empty")
    p = validate_portions(portions)
    return {"recipe_id": rid, "portions": p}
