# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: RecipeBoard
import json


def reset_demo_data():
    """Reset all recipe, ingredient, shopping-list, and user data to demo defaults."""
    global_recipes = {
        "id": 100,
        "name": "Spaghetti Bolognese",
        "ingredients": [
            {"item": "spaghetti", "quantity": 400, "unit": "g"},
            {"item": "ground beef", "quantity": 300, "unit": "g"},
            {"item": "tomato sauce", "quantity": 250, "unit": "ml"},
        ],
    }
    global_users = {
        "id": 1,
        "username": "demo_user",
        "email": "demo@example.com",
        "password_hash": "demo_hash_abc123",
    }
    global_shopping_lists = {
        "id": 50,
        "items": [
            {"item": "spaghetti", "quantity": 400},
            {"item": "ground beef", "quantity": 300},
            {"item": "tomato sauce", "quantity": 250},
        ],
    }

    with open("recipe_board_data.json", "w") as f:
        json.dump(
            {
                "recipes": global_recipes,
                "users": global_users,
                "shopping_lists": global_shopping_lists,
            },
            f,
        )


if __name__ == "__main__":
    reset_demo_data()
