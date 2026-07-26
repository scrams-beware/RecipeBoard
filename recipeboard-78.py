# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: RecipeBoard
def _parse_ingredient_line(line):
    """Split a line like '2 cups flour' into amount and ingredient."""
    parts = line.strip().split(None, 1)
    if len(parts) != 2:
        raise ValueError(f"Invalid ingredient format: {line!r}")
    return parts[0], parts[1]

def _clean_unit(unit):
    """Normalize common unit aliases to a canonical form."""
    aliases = {
        "cups": "cup", "tsp": "tsp", "tbsp": "tbsp",
        "oz": "oz", "lb": "lb", "g": "g", "kg": "kg",
        "ml": "ml", "l": "liter", "liters": "liter",
    }
    return aliases.get(unit.lower(), unit.lower())

def _format_unit(amount, unit):
    """Return a nicely formatted quantity string."""
    if amount == 1:
        u = unit.rstrip("s") + "s" if unit.endswith("s") else unit + "s"
        return f"{amount} {u}"
    return f"{amount:.2f} {unit}"

def _calc_unit_price(unit):
    """Return a placeholder price per common unit (used when no price given)."""
    prices = {"cup": 0.5, "tsp": 0.01, "tbsp": 0.03, "oz": 0.25,
              "lb": 4.99, "g": 0.02, "kg": 4.99, "ml": 0.01,
              "liter": 2.99}
    return prices.get(_clean_unit(unit), 0)

def _parse_ingredient(line):
    """Parse an ingredient line into (amount, unit, name)."""
    amount_str, rest = _parse_ingredient_line(line)
    if not amount_str.strip():
        raise ValueError(f"No quantity found in: {line!r}")
    try:
        amount = float(amount_str)
    except ValueError as e:
        raise ValueError(f"Bad number '{amount_str}' in line: {line!r}") from e

    unit, name = rest.split(None, 1) if " " in rest else ("", rest.strip())
    return amount, _clean_unit(unit), name
