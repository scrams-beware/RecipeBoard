# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: RecipeBoard
SAMPLE_TRANSCRIPTS = """\
>>> from recipe_board import RecipeBoard
>>> board = RecipeBoard()
>>> board.add_recipe("Pasta", [
...     {"name": "spaghetti", "amount": 400, "unit": "g"},
...     {"name": "tomato sauce", "amount": 250, "unit": "ml"},
...     {"name": "garlic", "amount": 3, "unit": "cloves"}])
>>> board.add_recipe("Salad", [
...     {"name": "lettuce", "amount": 1, "unit": "head"},
...     {"name": "tomato", "amount": 2, "unit": "pcs"},
...     {"name": "olive oil", "amount": 30, "unit": "ml"}])
>>> board.add_ingredient_price("spaghetti", 1.80)
>>> board.add_ingredient_price("garlic", 0.50)
>>> board.add_ingredient_price("tomato sauce", 2.10)
>>> board.set_portion_factor(2)
>>> print(board.build_shopping_list())
{'spaghetti': '400g', 'tomato sauce': '250ml', 'garlic': '3 cloves', 'lettuce': '1 head', 'tomato': '2 pcs', 'olive oil': '30ml'}
>>> board.calculate_total_cost()
6.90
"""
