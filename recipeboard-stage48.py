# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: RecipeBoard
import unittest
from recipe_board.core import Recipe, Ingredient, ShoppingList


class TestRecipe(unittest.TestCase):
    def test_create_recipe(self):
        r = Recipe(name="Pasta", ingredients=[Ingredient("spaghetti", 200)], portions=4)
        self.assertEqual(r.name, "Pasta")
        self.assertEqual(len(r.ingredients), 1)
        self.assertEqual(r.portions, 4)

    def test_recipe_total_cost(self):
        r = Recipe(name="Salad", ingredients=[Ingredient("lettuce", 50)], portions=2)
        self.assertAlmostEqual(r.total_cost(), 50.0)


class TestShoppingList(unittest.TestCase):
    def test_create_shopping_list(self):
        sl = ShoppingList()
        sl.add(Ingredient("eggs", 1))
        sl.add(Ingredient("milk", 2))
        self.assertEqual(len(sl), 2)

    def test_invalid_portions(self):
        with self.assertRaises(ValueError):
            Ingredient("bad", -1)


if __name__ == "__main__":
    unittest.main()
