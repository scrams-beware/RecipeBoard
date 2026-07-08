# === Stage 36: Add templates for quickly creating common records ===
# Project: RecipeBoard
class RecipeTemplates:
    """Quickly create common record templates for RecipeBoard."""

    @staticmethod
    def ingredient_template(name, quantity, unit, cost=None):
        """Create a standard ingredient template with optional cost."""
        return {
            "name": name,
            "quantity": quantity,
            "unit": unit,
            "cost": cost
        }

    @staticmethod
    def recipe_template(recipe_name, ingredients, portions=4, total_cost=None):
        """Create a basic recipe record with ingredient list and portion info."""
        return {
            "name": recipe_name,
            "ingredients": ingredients,
            "portions": portions,
            "total_cost": total_cost
        }

    @staticmethod
    def shopping_list_template(items=None):
        """Create a shopping list with optional initial items."""
        if items is None:
            items = []
        return {
            "items": items,
            "created_at": datetime.now(),
            "notes": ""
        }

    @staticmethod
    def menu_plan_template(date, recipes=None):
        """Create a daily menu plan with optional recipe list."""
        if recipes is None:
            recipes = []
        return {
            "date": date,
            "recipes": recipes,
            "notes": ""
        }

    @staticmethod
    def cost_check_template(recipes, budget):
        """Create a cost check record comparing recipe costs to budget."""
        total_cost = sum(r.get("total_cost", 0) for r in recipes if r.get("total_cost"))
        return {
            "recipes": recipes,
            "budget": budget,
            "actual_cost": total_cost,
            "within_budget": total_cost <= budget if budget else None,
            "remaining": budget - total_cost if budget and total_cost <= budget else 0
        }
