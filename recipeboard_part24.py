# === Stage 24: Add grouped summaries by category or status ===
# Project: RecipeBoard
def generate_grouped_summary(recipes, categories=None):
    if categories is None:
        categories = ['Vegetarian', 'Meat', 'Dairy']
    grouped = {cat: [] for cat in categories}
    total_cost = 0.0
    for recipe in recipes:
        cost = sum(item['price'] * item['quantity'] for item in recipe.get('ingredients', []))
        if recipe.get('category') and recipe['category'] in grouped:
            grouped[recipe['category']].append({'name': recipe['name'], 'cost': round(cost, 2)})
            total_cost += cost
    summary = {'total_estimated_cost': round(total_cost, 2), 'by_category': {k: [item for item in v if item] for k, v in grouped.items()}}
    return summary
