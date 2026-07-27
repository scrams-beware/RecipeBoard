# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: RecipeBoard
def run_demo():
    from recipe_board import (Ingredient, Recipe, ShoppingList, MenuPlan)

    flour = Ingredient("flour", price=1.50)
    sugar = Ingredient("sugar", price=2.00)
    eggs = Ingredient("eggs", price=3.50)
    butter = Ingredient("butter", price=4.00)

    cake_recipe = Recipe(name="Chocolate Cake", ingredients=[flour, sugar, eggs, butter], portions=8)
    soup_recipe = Recipe(name="Tomato Soup", ingredients=[sugar, butter], portions=4)

    print(f"📖 {cake_recipe.name}: serves {cake_recipe.portions} portions")
    print(f"   Cost per portion: ${cake_recipe.cost_per_portion():.2f}")
    print()

    sl = ShoppingList()
    sl.add(cake_recipe, 1)
    sl.add(soup_recipe, 2)
    print("🛒 Shopping List:")
    for item in sl:
        print(f"   - {item.name}: {item.quantity}x (${item.total:.2f})")
    print(f"   Total: ${sl.total_cost():.2f}")
    print()

    plan = MenuPlan()
    plan.add(cake_recipe, 1)
    plan.add(soup_recipe, 2)
    print("🗓️ Menu Plan:")
    for entry in plan:
        print(f"   - {entry.name}: {entry.quantity}x (Cost per portion: ${entry.cost_per_portion():.2f})")
    total = sum(entry.total_cost() * entry.quantity for entry in plan)
    print(f"\n💰 Total menu cost: ${total:.2f}")

run_demo()
