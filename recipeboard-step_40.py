# === Stage 40: Add plain text report export ===
# Project: RecipeBoard
def export_report(recipe_board, output_path="recipeboard_report.txt"):
    """Export a plain-text summary report of the RecipeBoard."""
    with open(output_path, "w") as f:
        f.write(f"RecipeBoard Report\n")
        f.write(f"{'=' * 40}\n")

        if recipe_board.recipes:
            for r in recipe_board.recipes:
                f.write(f"\n--- {r.name} ---\n")
                f.write(f"Portions: {r.portions}\n")
                total_cost = sum(ing.cost for ing in r.ingredients.values())
                per_portion = total_cost / r.portions if r.portions else 0
                f.write(f"Total cost: ${total_cost:.2f} ({per_portion:.2f}/portion)\n")

        if recipe_board.shopping_lists:
            for i, sl in enumerate(recipe_board.shopping_lists):
                f.write(f"\n--- Shopping List {i + 1} ---\n")
                total = sum(item["cost"] for item in sl.items)
                f.write(f"Items: {len(sl.items)} | Total: ${total:.2f}\n")

        if recipe_board.cost_checks:
            f.write("\n--- Cost Checks ---\n")
            for check in recipe_board.cost_checks:
                f.write(f"{check['recipe']}: {'OK' if not check['over_budget'] else 'OVER BUDGET'} (${check['total']:.2f}/$ {check['budget']})\n")

        f.write("\n--- End of Report ---\n")
