# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: RecipeBoard
from typing import Optional, List, Dict, Any


def parse_ingredient_line(line: str) -> Optional[Dict[str, Any]]:
    """Parse a single ingredient line into a structured dict."""
    parts = line.split(":", 1)
    if len(parts) != 2:
        return None
    name = parts[0].strip()
    value_str = parts[1].strip()
    try:
        amount = float(value_str.replace(",", "."))
    except ValueError:
        return None
    unit = "g"
    if any(unit in value_str for unit in ["kg", "l", "ml", "ml.", ", kg"]):
        unit = value_str.split()[-1]
    else:
        unit = value_str.split()[-1].lower()
    return {"name": name, "amount": amount, "unit": unit}


def calculate_total_cost(ingredients: List[Dict[str, Any]], prices: Dict[str, float]) -> float:
    """Calculate the total cost of a list of ingredients based on their prices."""
    total = 0.0
    for ing in ingredients:
        if ing["name"] in prices:
            price_per_unit = prices[ing["name"]]
            total += price_per_unit * ing["amount"] / (1000.0 if ing["unit"] == "kg" else 1)
    return round(total, 2)


def format_cost_report(total: float, budget: Optional[float] = None) -> str:
    """Format a cost report string."""
    lines = ["Total Cost:", f"${total:.2f}"]
    if budget is not None:
        remaining = budget - total
        status = "within budget" if remaining >= 0 else "over budget"
        lines.append(f"Budget: ${budget:.2f}")
        lines.append(f"Remaining: ${remaining:.2f} ({status})")
    return "\n".join(lines)


def validate_recipe_ingredients(ing_list: List[Dict[str, Any]], min_count: int = 1) -> bool:
    """Validate that a recipe has at least a minimum number of ingredients."""
    return len(ing_list) >= min_count
