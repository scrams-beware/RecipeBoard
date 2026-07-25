# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: RecipeBoard
def generate_validation_report(ingredients, portions, recipe_name):
    warnings = []
    errors = []
    if not recipe_name:
        errors.append("Recipe name is empty.")
    for i, ing in enumerate(ingredients):
        if not ing['name']:
            errors.append(f"Ingredient {i+1} has no name.")
        elif ing['quantity'] <= 0:
            errors.append(f"Ingredient '{ing['name']}' has non-positive quantity ({ing['quantity']}).")
        elif ing['unit'] is None or str(ing['unit']).strip() == '':
            warnings.append(f"Ingredient '{ing['name']}' missing unit.")
    if portions <= 0:
        errors.append("Portions must be a positive number.")
    else:
        for i, ing in enumerate(ingredients):
            if ing['quantity'] < portions * 2:
                warnings.append(f"Ingredient '{ing['name']}' may not serve {portions} people (qty={ing['quantity']}).")
    return {'warnings': warnings, 'errors': errors}
