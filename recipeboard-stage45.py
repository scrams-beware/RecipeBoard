# === Stage 45: Add restore from backup with validation ===
# Project: RecipeBoard
def restore_backup(backup_path, data_dir="data"):
    """Restore RecipeBoard state from a JSON backup with basic validation."""
    import json, os

    if not os.path.isfile(backup_path):
        raise FileNotFoundError(f"Backup file not found: {backup_path}")

    try:
        with open(backup_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        raise ValueError(f"Invalid backup JSON: {e}")

    if not isinstance(data, dict):
        raise ValueError("Backup must be a JSON object at the top level")

    required_keys = {"recipes", "ingredients", "shopping_lists"}
    missing = required_keys - set(data.keys())
    if missing:
        raise KeyError(f"Missing required keys in backup: {missing}")

    for key in ["recipes", "ingredients"]:
        if not isinstance(data[key], list):
            raise TypeError(f"'{key}' must be a list")

    os.makedirs(data_dir, exist_ok=True)
    out_path = os.path.join(data_dir, "state.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Restored {len(data['recipes'])} recipes and {len(data['ingredients'])} ingredients.")
    return out_path
