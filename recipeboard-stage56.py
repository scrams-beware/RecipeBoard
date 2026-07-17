# === Stage 56: Add compact error classes for domain failures ===
# Project: RecipeBoard
class RecipeBoardError(Exception):
    pass


class IngredientNotFoundError(RecipeBoardError):
    def __init__(self, ingredient_name: str):
        super().__init__(f"Ingredient '{ingredient_name}' not found in any recipe.")
        self.ingredient_name = ingredient_name


class PortionMismatchError(RecipeBoardError):
    def __init__(self, expected: int, actual: int):
        super().__init__(f"Portion mismatch: expected {expected}, got {actual}.")
        self.expected_portions = expected
        self.actual_portions = actual


class InsufficientFundsError(RecipeBoardError):
    def __init__(self, total_cost: float, balance: float):
        super().__init__(f"Insufficient funds. Recipe cost is {total_cost}, balance is {balance}.")
        self.total_cost = total_cost
        self.balance = balance


class ShoppingListConflictError(RecipeBoardError):
    def __init__(self, recipe_name: str):
        super().__init__(f"Multiple conflicting entries for '{recipe_name}' in the shopping list.")
        self.recipe_name = recipe_name


class InvalidMenuDateError(RecipeBoardError):
    def __init__(self, date_str: str):
        super().__init__(f"Invalid menu date format: {date_str}. Expected YYYY-MM-DD.")
        self.date_str = date_str


class DuplicateEntryError(RecipeBoardError):
    def __init__(self, entry_type: str, identifier: str):
        super().__init__(f"Duplicate {entry_type} found with identifier '{identifier}'.")
        self.entry_type = entry_type
        self.identifier = identifier
