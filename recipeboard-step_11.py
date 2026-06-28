# === Stage 11: Add JSON export for the current application state ===
# Project: RecipeBoard
def export_state_to_json(state: dict, filename: str = "recipeboard_export.json"):
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
