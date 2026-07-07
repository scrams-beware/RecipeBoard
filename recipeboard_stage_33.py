# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: RecipeBoard
def get_settings():
    return {
        "default_portions": 4,
        "currency_symbol": "$",
        "max_shopping_list_size": 50,
        "show_total_cost": True,
        "sort_ingredients_alphabetically": False,
        "cost_threshold_warning": 20.0,
    }

def update_settings(settings_dict):
    allowed_keys = {
        "default_portions", "currency_symbol", "max_shopping_list_size",
        "show_total_cost", "sort_ingredients_alphabetically", "cost_threshold_warning"
    }
    for key in settings_dict:
        if key not in allowed_keys:
            raise ValueError(f"Unknown setting key: {key}")
    return {**get_settings(), **settings_dict}

def reset_settings():
    return get_settings()
