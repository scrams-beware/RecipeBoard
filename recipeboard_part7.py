# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: RecipeBoard
def format_ingredient(ing: dict, price_per_unit: float = None) -> str:
    name = ing.get("name", "Unknown")
    amount = ing.get("amount", 0)
    unit = ing.get("unit", "")
    if price_per_unit is not None and amount > 0:
        cost = round(amount * price_per_unit, 2)
        return f"• {name}: {amount} {unit} — ${cost}"
    return f"• {name}: {amount} {unit}"

def format_shopping_list(items: list[dict], prices: dict[str, float]) -> str:
    lines = []
    for item in items:
        name = item.get("name", "")
        amount = item.get("amount", 0)
        unit = item.get("unit", "")
        if name and amount > 0:
            price = prices.get(name, 0)
            cost = round(amount * price, 2) if price else "?"
            lines.append(format_ingredient({"name": name, "amount": amount, "unit": unit}, price))
    return "\n".join(lines)

def format_recipe_summary(recipe: dict) -> str:
    title = recipe.get("title", "Untitled")
    servings = recipe.get("servings", 1)
    total_cost = round(recipe.get("total_cost", 0), 2)
    prep_time = recipe.get("prep_time_min", 0)
    lines = [f"=== {title} ==="]
    if servings:
        lines.append(f"Servings: {servings}")
    if total_cost is not None and total_cost > 0:
        lines.append(f"Total Cost: ${total_cost:.2f}")
    if prep_time:
        lines.append(f"Prep Time: {prep_time} min")
    return "\n".join(lines)

def format_menu_plan(meal_plan: list[dict]) -> str:
    lines = ["📅 Menu Plan"]
    for day in meal_plan:
        date = day.get("date", "Unknown Date")
        meals = day.get("meals", [])
        if not meals:
            continue
        lines.append(f"\n{date}:")
        for meal_type, recipe_ref in meals.items():
            if isinstance(recipe_ref, dict):
                title = recipe_ref.get("title", "Unknown Recipe")
                cost = round(recipe_ref.get("total_cost", 0), 2)
                lines.append(f"  • {meal_type.capitalize()}: {title} (${cost:.2f})")
            else:
                lines.append(f"  • {meal_type.capitalize()}: Custom ({recipe_ref})")
    return "\n".join(lines)
