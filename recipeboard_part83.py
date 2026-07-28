# === Stage 83: Add regression tests for the final demo workflow ===
# Project: RecipeBoard
def test_recipe_board_workflow():
    """Regression test for RecipeBoard demo workflow."""
    from recipe_board import Recipe, ShoppingList, MenuPlan, CostTracker

    # Create a simple recipe
    recipe = Recipe(name="Pasta", ingredients={"spaghetti": 2.0, "tomato sauce": 3.5}, portions=4)
    assert len(recipe.ingredients) == 2
    assert recipe.portions == 4

    # Calculate cost per portion
    total_cost = sum(v for v in recipe.ingredients.values())
    cost_per_portion = total_cost / recipe.portions
    assert abs(cost_per_portion - 1.375) < 0.001

    # Create a shopping list
    shopping_list = ShoppingList(items=[("spaghetti", 2), ("tomato sauce", 4)])
    assert len(shopping_list.items) == 2

    # Create a menu plan
    menu_plan = MenuPlan(meals={"dinner": [recipe]})
    assert "dinner" in menu_plan.meals
    assert len(menu_plan.meals["dinner"]) == 1

    # Track costs over time
    tracker = CostTracker()
    tracker.add_entry(recipe, date="2024-01-15")
    tracker.add_entry(recipe, date="2024-01-16")
    assert len(tracker.entries) == 2

    # Verify average cost calculation
    avg_cost = sum(e.cost for e in tracker.entries) / len(tracker.entries)
    assert abs(avg_cost - 1.375) < 0.001

    print("All regression tests passed!")
    return True
