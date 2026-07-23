# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: RecipeBoard
def seed_demo_data():
    """Populate RecipeBoard with deterministic sample data for quick demo."""
    from recipe_board import Board, Ingredient, ShoppingList, MenuDay

    board = Board("Demo Kitchen")
    ingredients = [
        Ingredient("Rice", 5.0),
        Ingredient("Tomato Sauce", 3.5),
        Ingredient("Chicken Breast", 8.99),
        Ingredient("Olive Oil", 6.49),
        Ingredient("Garlic", 1.29),
    ]

    board.add_ingredients(ingredients)
    board.set_portions_default(4)

    recipe = board.new_recipe("Classic Bolognese")
    recipe.add_ingredient("Rice", 0.3)
    recipe.add_ingredient("Tomato Sauce", 0.5)
    recipe.add_ingredient("Chicken Breast", 0.2)
    recipe.add_ingredient("Olive Oil", 0.1)
    recipe.add_ingredient("Garlic", 0.05)

    board.add_recipe(recipe, cost_per_serving=3.47)

    sl = ShoppingList.from_board(board)
    for ing in ingredients:
        if ing.name != "Rice":
            sl.add(ing, quantity=2)
    board.set_shopping_list(sl)

    menu = MenuDay("Monday")
    menu.dishes.append(("Classic Bolognese", 1))
    board.set_menu(menu)

    return board


if __name__ == "__main__":
    demo = seed_demo_data()
    print(f"Board: {demo.name}, Recipes: {len(demo.recipes)}, Shopping items: {len(demo.shopping_list)}")
