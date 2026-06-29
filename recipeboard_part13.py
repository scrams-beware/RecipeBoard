# === Stage 13: Add file save support using a configurable path ===
# Project: RecipeBoard
import os
from pathlib import Path

def save_recipe(recipe: dict, path: str = "recipes.json") -> None:
    """Save a single recipe to JSON with configurable file path."""
    try:
        data_path = Path(path)
        if not data_path.exists():
            data_path.parent.mkdir(parents=True, exist_ok=True)
        
        import json
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(recipe, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving recipe to {path}: {e}")

def load_recipes(path: str = "recipes.json") -> list[dict]:
    """Load all recipes from the configured JSON file."""
    try:
        data_path = Path(path)
        if not data_path.exists():
            return []
        
        import json
        with open(data_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except Exception as e:
        print(f"Error loading recipes from {path}: {e}")
        return []

def save_shopping_list(items: list[str], path: str = "shopping.json") -> None:
    """Save the shopping list to a separate JSON file."""
    try:
        data_path = Path(path)
        if not data_path.exists():
            data_path.parent.mkdir(parents=True, exist_ok=True)
        
        import json
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving shopping list to {path}: {e}")

def load_shopping_list(path: str = "shopping.json") -> list[str]:
    """Load the shopping list from a separate JSON file."""
    try:
        data_path = Path(path)
        if not data_path.exists():
            return []
        
        import json
        with open(data_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except Exception as e:
        print(f"Error loading shopping list from {path}: {e}")
        return []
