# === Stage 51: Add unit tests for search and filter behavior ===
# Project: RecipeBoard
import unittest
from recipe_board.models import Recipe, Ingredient, ShoppingItem

class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        self.recipes = [
            Recipe(id=1, name="Pasta", ingredients=[Ingredient("pasta", 200), Ingredient("tomato sauce", 50)], cost_per_person=3.5),
            Recipe(id=2, name="Salad", ingredients=[Ingredient("lettuce", 100), Ingredient("cucumber", 80)], cost_per_person=2.0),
            Recipe(id=3, name="Stir Fry", ingredients=[Ingredient("rice", 150), Ingredient("soy sauce", 40), Ingredient("vegetables", 60)], cost_per_person=4.5),
        ]

    def test_search_by_name(self):
        results = Recipe.search_by_name(self.recipes, "Pasta")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Pasta")

    def test_filter_by_max_cost(self):
        results = Recipe.filter_by_max_cost(self.recipes, 3.5)
        self.assertTrue(all(r.cost_per_person <= 3.5 for r in results))
        self.assertEqual(len(results), 2)

    def test_search_and_filter_combined(self):
        filtered = [r for r in self.recipes if r.name.startswith("S")]
        cheap = Recipe.filter_by_max_cost(filtered, 3.0)
        self.assertGreaterEqual(len(cheap), 1)

    def test_search_no_match(self):
        results = Recipe.search_by_name(self.recipes, "Steak")
        self.assertEqual(results, [])

if __name__ == "__main__":
    unittest.main()
