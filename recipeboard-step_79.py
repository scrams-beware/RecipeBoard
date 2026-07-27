# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: RecipeBoard
def self_check(boards, recipes):
    print("=== RecipeBoard Self-Check ===")
    for board in boards:
        try:
            assert board.name and len(board.receipts) == 0, "Empty or invalid board"
        except AssertionError as e:
            print(f"FAIL: {board.name} - {e}")
            continue
        print(f"OK: Board '{board.name}' has {len(board.receipts)} receipts")

    for recipe in recipes.values():
        try:
            assert len(recipe.ingredients) > 0 and isinstance(recipe.cost, (int, float))
        except AssertionError as e:
            print(f"FAIL: Recipe '{recipe.title}' - {e}")
            continue
        print(f"OK: Recipe '{recipe.title}' costs {recipe.cost:.2f} for {recipe.portions} portions")

    demo = Board("Demo", "demo@example.com")
    sample_recipe = recipes.get("sample", None) or {"title": "Sample", "ingredients": [{"name": "flour", "amount": 1}], "cost": 0.5, "portions": 2}
    receipt = Receipt(
        recipe=sample_recipe, portions=3, date="2025-06-01",
        ingredients=[{"name": "flour", "amount": 1.5}]
    )
    demo.add_receipt(receipt)
    print(f"OK: Demo board created with {len(demo.receipts)} receipts")

    total = sum(r.total_cost for r in demo.receipts)
    assert total > 0, "Demo receipt should have positive cost"
    print(f"OK: Total demo cost is {total:.2f}")

    print("=== Self-Check Complete ===")
