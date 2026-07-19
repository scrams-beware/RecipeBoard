# === Stage 60: Add saved views for frequently used filters ===
# Project: RecipeBoard
import json
from pathlib import Path

class RecipeBoard:
    def __init__(self):
        self.recipes = {}
        self.shopping_lists = []
        self.saved_views = {}

    def add_recipe(self, name, ingredients, portions=4, cost=None):
        self.recipes[name] = {"name": name, "ingredients": ingredients, "portions": portions, "cost": cost}

    def get_total_cost(self, recipe_name, target_portions=None):
        if recipe_name not in self.recipes:
            return 0.0
        r = self.recipes[recipe_name]
        base_cost = sum(i["unit_price"] * (i["quantity"] / r["portions"]) for i in r["ingredients"])
        cost_per_portion = base_cost if r["cost"] is None else r["cost"]
        return cost_per_portion * target_portions if target_portions else base_cost

    def create_shopping_list(self, recipe_name):
        if recipe_name not in self.recipes:
            return {}
        needed = {}
        for ing in self.recipes[recipe_name]["ingredients"]:
            name = ing["name"]
            qty = ing["quantity"] / self.recipes[recipe_name]["portions"]
            needed[name] = {
                "ingredient": name,
                "unit_price": ing["unit_price"],
                "required_qty": qty * self.get_target_portions(recipe_name),
                "needed_in_total": 0.0,
                "left_in_stock": 0.0
            }
        return needed

    def update_shopping_list(self, recipe_name):
        if recipe_name not in self.recipes:
            return {}
        needed = self.create_shopping_list(recipe_name)
        for ing in self.recipes[recipe_name]["ingredients"]:
            name = ing["name"]
            if name in needed:
                needed[name]["needed_in_total"] += ing["quantity"] / self.get_target_portions(recipe_name) * ing["unit_price"]
        return needed

    def save_view(self, view_id, filters):
        self.saved_views[view_id] = {"id": view_id, "filters": filters}

    def load_saved_view(self, view_id):
        if view_id not in self.saved_views:
            raise ValueError(f"View {view_id} not found.")
        return self.saved_views[view_id]["filters"]

    def list_saved_views(self):
        return [{"id": v["id"], "filters": v["filters"]} for v in self.saved_views.values()]

# Example usage
if __name__ == "__main__":
    rb = RecipeBoard()
    rb.add_recipe("Pasta", [
        {"name": "Spaghetti", "quantity": 400, "unit_price": 1.5},
        {"name": "Tomato Sauce", "quantity": 200, "unit_price": 3.0},
        {"name": "Garlic", "quantity": 5, "unit_price": 0.8}
    ], portions=4)
    rb.add_recipe("Salad", [
        {"name": "Lettuce", "quantity": 200, "unit_price": 2.0},
        {"name": "Tomato", "quantity": 150, "unit_price": 1.5}
    ], portions=2)
    rb.create_shopping_list("Pasta")
    print(rb.list_saved_views())
