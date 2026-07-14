# === Stage 50: Add unit tests for import and export behavior ===
# Project: RecipeBoard
import json, os
from pathlib import Path
from recipeboard.core.data_models import Ingredient, Recipe, ShoppingListEntry
from recipeboard.core.recipe_manager import RecipeManager

def test_import_export_roundtrip(tmp_path):
    manager = RecipeManager()
    ing = Ingredient(name="chicken", qty=2.0, unit="kg", price_per_unit=15.0)
    recipe = Recipe(
        name="Grilled Chicken",
        ingredients=[ing],
        portions=4,
        prep_time_minutes=30,
        cook_time_minutes=25,
        category="Main"
    )
    manager.add_recipe(recipe)
    assert len(manager.recipes) == 1
    assert recipe.name in {r.name for r in manager.recipes}

    with open(tmp_path / "recipes.json", "w") as f:
        json.dump([recipe.to_dict()], f, indent=2)
    loaded = [Recipe.from_dict(d) for d in json.load(open(tmp_path / "recipes.json"))]
    assert len(loaded) == 1
    assert loaded[0].name == recipe.name
    assert loaded[0].ingredients[0].qty == ing.qty

def test_import_export_shopping_list():
    entries = [ShoppingListEntry(name="onion", qty=3, unit="pcs", notes="red") for _ in range(2)]
    sl = ShoppingList(entries=entries)
    assert len(sl.entries) == 2
    data = {"name": "Test List", "entries": [e.to_dict() for e in entries]}
    with open(tmp_path / "shop.json", "w") as f:
        json.dump(data, f)
    loaded = ShoppingList.from_dict(json.load(open(tmp_path / "shop.json")))
    assert len(loaded.entries) == 2
    assert loaded.entries[0].name == entries[0].name

if __name__ == "__main__":
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        test_import_export_roundtrip(Path(td))
        test_import_export_shopping_list()
    print("All import/export tests passed")
