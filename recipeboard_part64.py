# === Stage 64: Add validation for relationship references ===
# Project: RecipeBoard
def validate_references(self):
    errors = []
    
    for recipe in self.recipes:
        if not recipe.id:
            errors.append("Recipe missing id")
        else:
            for ingredient in recipe.ingredients:
                if ingredient.recipe_id != recipe.id:
                    errors.append(f"Ingredient {ingredient.id} has wrong recipe_id")
        
        if recipe.portions is None and recipe.cost_per_serving is not None:
            errors.append("Cannot have cost_per_serving without portions")

    for shopping_list in self.shopping_lists:
        if not shopping_list.id:
            errors.append("Shopping list missing id")
        else:
            for item in shopping_list.items:
                if item.shopping_list_id != shopping_list.id:
                    errors.append(f"Item {item.id} has wrong shopping_list_id")

    return len(errors) == 0, errors
