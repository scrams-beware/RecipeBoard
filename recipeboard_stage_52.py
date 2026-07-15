# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: RecipeBoard
def format_ingredient_row(ingredient: Ingredient, budget_per_item: float) -> str:
    """Return a formatted string for an ingredient row in the planning board."""
    total_cost = round(ingredient.total_cost, 2)
    remaining = max(budget_per_item - total_cost, 0.01)
    status_icon = "✓" if remaining > 0 else "✗"
    return (f"{status_icon} {ingredient.name:30s} | "
            f"{ingredient.portions_needed:>4d} | "
            f"${total_cost:.2f} | ${remaining:.2f}")

def format_menu_summary(menu_plan: MenuPlan) -> str:
    """Return a formatted summary of the menu plan for display."""
    lines = ["📋 RecipeBoard Menu Plan"]
    lines.append("=" * 50)
    total_cost = sum(ingredient.total_cost for ingredient in menu_plan.ingredients)
    lines.append(f"Total Cost: ${total_cost:.2f}")
    if menu_plan.shopping_list:
        lines.append("Shopping List:")
        for item in menu_plan.shopping_list:
            lines.append(f"  - {item}")
    return "\n".join(lines)

def validate_ingredient_name(name: str) -> None:
    """Raise ValueError if ingredient name is empty or contains non-alphanumeric chars."""
    if not name or not name.strip():
        raise ValueError("Ingredient name must be a non-empty string.")
    if not re.match(r"^[a-zA-Z0-9\-\s]+$", name):
        raise ValueError(f"Invalid character in ingredient name: '{name}'")

def check_budget_feasibility(ingredients: list[Ingredient], budget_per_item: float) -> dict[str, bool]:
    """Check if all ingredients fit within the per-item budget; return a status dict."""
    results = {}
    for ingredient in ingredients:
        fits = ingredient.total_cost <= budget_per_item
        results[f"{ingredient.name}"] = fits
    return results

def calculate_total_menu_budget(menu_plan: MenuPlan) -> float:
    """Calculate the total cost of all ingredients in a menu plan."""
    return round(sum(ingredient.total_cost for ingredient in menu_plan.ingredients), 2)

def get_shopping_items_from_ingredients(ingredients: list[Ingredient]) -> dict[str, int]:
    """Aggregate shopping items from multiple ingredients into a single list."""
    shopping = {}
    for ingredient in ingredients:
        if ingredient.shopping_item and ingredient.shopping_quantity > 0:
            item_name = ingredient.shopping_item
            qty = ingredient.shopping_quantity
            current_qty = shopping.get(item_name, 0)
            shopping[item_name] = current_qty + qty
    return shopping
