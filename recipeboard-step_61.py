# === Stage 61: Add performance timing for core list and search operations ===
# Project: RecipeBoard
import time

# Performance timing for core list and search operations in RecipeBoard
def benchmark_recipe_operations(ingredients, recipes):
    """Benchmark common operations on ingredients and recipe lists."""
    # List operations
    start = time.time()
    unique_ingredients = set(ingredient['name'] for ingredient in ingredients)
    total_unique_count = len(unique_ingredients)
    list_time = (time.time() - start) * 1000

    # Search operation: find all recipes containing a specific ingredient
    target_ingredient = "flour" if any("flour" in i['name'] for i in ingredients) else ingredients[0]['name']
    start = time.time()
    matching_recipes = [recipe for recipe in recipes if target_ingredient in [i['name'].lower() for ingredient_list in [r.get('ingredients', [])] for i in ingredient_list]]
    search_time = (time.time() - start) * 1000

    # List operations: filter by cost threshold
    max_cost = 5.0
    start = time.time()
    affordable_recipes = [recipe for recipe in recipes if recipe['total_cost'] <= max_cost]
    filter_time = (time.time() - start) * 1000

    print(f"List operations: {list_time:.3f}ms, Search: {search_time:.3f}ms, Filter: {filter_time:.3f}ms")
