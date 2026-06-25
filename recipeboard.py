# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: RecipeBoard
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import uuid

@dataclass
class Ingredient:
    name: str
    price_per_unit: float  # per kg or liter
    unit: str = "kg"
    
@dataclass 
class RecipeIngredient(Ingredient):
    quantity_needed: float
    
@dataclass
class Recipe:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    name: str
    ingredients: List[RecipeIngredient] = field(default_factory=list)
    
def init_board() -> Dict[str, 'Recipe']:
    recipes: Dict[str, Recipe] = {}
    
    def add_recipe(name: str, ing_data: List[tuple], price_map: Dict[str, float]) -> None:
        recipe = Recipe(name=name)
        for q, name in ing_data:
            base_ing = Ingredient(name=name, unit="kg", price_per_unit=price_map.get(name, 0))
            recipe.ingredients.append(RecipeIngredient(quantity_needed=q, **base_ing.__dict__))
        recipes[recipe.id] = recipe
        
    # Demo dataset with realistic prices (EUR)
    demo_prices: Dict[str, float] = {
        "flour": 1.5, "sugar": 2.0, "butter": 8.5, 
        "eggs": 4.5, "milk": 1.2, "chicken_breast": 9.0,
        "tomatoes": 3.5, "onions": 1.8, "pasta": 2.2
    }
    
    add_recipe("Simple_Pancakes", [(0.3, "flour"), (0.1, "sugar"), (0.05, "butter")], demo_prices)
    add_recipe("Chicken_Stir_Fry", [(150/1000, "chicken_breast"), (200/1000, "tomatoes"), (100/1000, "onions")], demo_prices)
    
    return recipes

# Usage example to verify state initialization
board = init_board()
for rid, recipe in board.items():
    print(f"Recipe: {recipe.name}, Cost: {sum(i.quantity_needed * i.price_per_unit for i in recipe.ingredients):.2f} EUR")
