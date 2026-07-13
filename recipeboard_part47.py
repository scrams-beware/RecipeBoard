# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: RecipeBoard
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) or '.')

from recipe_board import RecipeBoard

board = RecipeBoard()

# 1) Add a recipe with ingredients and portions
soup = board.add_recipe('Tomato Soup', {'tomatoes': '3 kg', 'onions': '2'}, portions=4, cost='€5.00')
pasta = board.add_recipe('Penne Primavera', {'penne': '250 g', 'spinach': '150 g', 'garlic': '3 cloves', 'olive oil': '2 tbsp'}, portions=2, cost='€4.20')

# 2) Plan a menu for a week
menu = ['Tomato Soup', 'Penne Primavera'] * 7 + ['Tomato Soup']
board.plan_menu(menu)

# 3) Generate shopping list and check costs
shopping, total_cost, recipe_count = board.get_shopping_list()

print(f'Planning {recipe_count} recipes')
print(f'Total estimated cost: {total_cost}')
print('Shopping list:')
for item in sorted(shopping):
    print(f'  - {item[0]} x{item[1]}  ({item[2]})')
