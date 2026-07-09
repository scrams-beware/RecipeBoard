# === Stage 37: Add recommendations for the next useful action ===
# Project: RecipeBoard
def suggest_next_action(recipe, current_step):
    """Suggest next useful action based on recipe progress."""
    if current_step < len(recipe.get("steps", [])):
        return f"Complete step {current_step + 1}: {recipe['steps'][current_step]}"
    elif "shopping_list" not in recipe:
        return "Generate shopping list from ingredients."
    elif "cost_estimate" not in recipe:
        return "Calculate cost estimate for this recipe."
    else:
        return "Review and verify the final budget summary."

def format_summary(recipe):
    """Return a compact text summary of the recipe."""
    lines = [f"Recipe: {recipe.get('name', 'Unknown')}"]
    if recipe.get("ingredients"):
        lines.append(f"Ingredients: {len(recipe['ingredients'])} items")
    if recipe.get("cost_estimate"):
        lines.append(f"Estimated Cost: ${recipe['cost_estimate']:.2f}")
    if recipe.get("shopping_list"):
        lines.append(f"Shopping List: {len(recipe['shopping_list'])} items")
    return "\n".join(lines)

def main():
    sample_recipe = {
        "name": "Pasta Carbonara",
        "ingredients": ["spaghetti", "pancetta", "eggs", "cheese", "pepper"],
        "steps": [
            {"step": 1, "instruction": "Boil water for pasta"},
            {"step": 2, "instruction": "Cook spaghetti al dente"},
            {"step": 3, "instruction": "Sauté pancetta until crispy"},
            {"step": 4, "instruction": "Mix eggs and cheese in a bowl"},
            {"step": 5, "instruction": "Combine pasta with sauce off heat"}
        ],
        "cost_estimate": 12.50,
        "shopping_list": ["spaghetti", "pancetta", "eggs", "cheese", "pepper"],
        "current_step": 3
    }

    print(format_summary(sample_recipe))
    next_action = suggest_next_action(sample_recipe, sample_recipe["current_step"])
    print(f"Next action: {next_action}")

if __name__ == "__main__":
    main()
