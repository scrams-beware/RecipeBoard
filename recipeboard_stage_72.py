# === Stage 72: Add Markdown report export ===
# Project: RecipeBoard
def export_report(shopping_list, recipes):
    """Export a compact Markdown report of the recipe board."""
    lines = ["# RecipeBoard Report", ""]
    if shopping_list:
        lines.append("## Shopping List")
        for item in shopping_list:
            qty_str = f"{item['quantity']} x {item['name']}" if 'quantity' in item else item['name']
            price_str = f" - ${item.get('price', 0):.2f}" if 'price' in item else ""
            lines.append(f"- {qty_str}{price_str}")
        total_cost = sum(item.get('price', 0) for item in shopping_list if 'price' in item)
        lines.append(f"\n**Total Estimated Cost: ${total_cost:.2f}**")
    if recipes:
        lines.append("")
        lines.append("## Recipes")
        for recipe in recipes:
            name = recipe.get('name', 'Unnamed')
            portions = recipe.get('portions', 1)
            cost_per_serving = recipe.get('cost_per_serving', 0)
            total_cost_recipe = cost_per_serving * portions
            lines.append(f"- {name} ({portions} portions, ${total_cost_recipe:.2f})")
    return "\n".join(lines)
