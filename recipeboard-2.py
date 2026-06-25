# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: RecipeBoard
from dataclasses import dataclass, field
from typing import Optional, List
from decimal import Decimal

@dataclass(frozen=True)
class Ingredient:
    name: str
    quantity: Decimal
    unit: str  # e.g., "g", "ml", "pcs"
    price_per_unit: Decimal = Decimal("0.00")

@dataclass
class Recipe:
    name: str
    description: Optional[str] = None
    ingredients: List[Ingredient] = field(default_factory=list)
    servings: int = 1
    
    def calculate_total_cost(self, ingredient_prices: dict[str, Decimal]) -> Decimal:
        total = Decimal("0.00")
        for ing in self.ingredients:
            unit_price = ingredient_prices.get(ing.name.lower(), Decimal("0.00"))
            cost = (unit_price * ing.quantity) / Decimal(str(ing.unit)) if ing.unit else unit_price
            # Simplified assumption: price_per_unit is per gram/ml, adjust based on actual quantity needed
            total += ing.quantity * unit_price
        return round(total, 2)

@dataclass
class ShoppingItem:
    ingredient_name: str
    required_quantity: Decimal
    available_quantity: Optional[Decimal] = None
    
    def check_availability(self) -> bool:
        if self.available_quantity is None:
            return True
        return self.available_quantity >= self.required_quantity

@dataclass
class DailyMenu:
    date: str
    recipes: List[Recipe] = field(default_factory=list)
    
    def generate_shopping_list(self, pantry: dict[str, Decimal]) -> List[ShoppingItem]:
        items = []
        for recipe in self.recipes:
            for ing in recipe.ingredients:
                item = ShoppingItem(
                    ingredient_name=ing.name,
                    required_quantity=ing.quantity,
                    available_quantity=pantry.get(ing.name.lower(), Decimal("0"))
                )
                items.append(item)
        return items
