# === Stage 66: Add export of a short status dashboard ===
# Project: RecipeBoard
def dashboard():
    print("=" * 35)
    print("   RecipeBoard — Quick Status")
    print("=" * 35)
    if recipes:
        print(f"Recipes loaded : {len(recipes)}")
        for r in recipes:
            print(f"  • {r['name']}  →  cost={r.get('cost', 'N/A')} / portions={r.get('portions', '?')}")
    else:
        print("No recipes yet.")
    if shopping_lists:
        print(f"\nShopping lists : {len(shopping_lists)}")
        for sl in shopping_lists:
            items = [i for i in sl['items'] if i.get('qty', 0) > 0]
            if items:
                print(f"  • {sl['name']} → {len(items)} item(s)")
    if budget_log:
        total_spent = sum(v['spent'] for v in budget_log.values())
        print(f"\nBudget spent   : ${total_spent:.2f} / ${budget_limit:.2f}")
        if total_spent > budget_limit:
            print("  ⚠ Budget exceeded!")
    print("\nPress Ctrl+C to exit.")
