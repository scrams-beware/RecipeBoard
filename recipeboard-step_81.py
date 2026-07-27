# === Stage 81: Add final README text as a module string with usage examples ===
# Project: RecipeBoard
def usage_examples():
    """Demonstrate key RecipeBoard features with minimal examples."""
    from recipe_board import Recipe, ShoppingList, BudgetTracker

    # Create a simple recipe
    recipe = Recipe(
        name="Spaghetti Bolognese",
        ingredients=[("spaghetti", 1.50), ("ground beef", 3.99), ("tomato sauce", 2.49)],
        portions=4,
        prep_time_minutes=30,
    )

    # Track budget over multiple days of cooking
    tracker = BudgetTracker()
    tracker.add_expense("Spaghetti Bolognese", recipe.cost())
    print(f"Total spent: ${tracker.get_total():.2f}")

    # Plan a shopping list for the week
    sl = ShoppingList()
    sl.add_item("ground beef", 3.99, quantity=2)
    sl.display_summary()
