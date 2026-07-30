# === Stage 88: Add safer defaults for empty input and missing optional fields ===
# Project: RecipeBoard
def safe_float(value, default=0.0):
    """Convert to float safely; return a default on failure."""
    if value is None:
        return default
    try:
        return float(str(value).strip())
    except (ValueError, TypeError):
        return default

def safe_int(value, default=0):
    """Convert to int safely; return a default on failure."""
    if value is None:
        return default
    try:
        return int(float(str(value).strip()))
    except (ValueError, TypeError):
        return default

def ensure_non_empty(value, default=None):
    """Return the trimmed string or a fallback when empty."""
    s = str(value).strip() if value is not None else ""
    return s if s else default

def safe_portions(value, default=1):
    """Ensure portions is at least 1; raise on zero/negative."""
    p = float(safe_float(value)) or 0
    if p <= 0:
        raise ValueError("portions must be positive")
    return int(p)

def safe_cost(value, default=0.0):
    """Return a non-negative cost; treat empty/None as zero."""
    c = float(safe_float(value)) or 0
    return max(c, 0.0)

def normalize_ingredient(name, amount=None):
    """Strip and lowercase ingredient name; keep amount if valid else None."""
    n = str(name).strip().lower() if name is not None else ""
    a = safe_float(amount) if amount is not None else None
    return (n or "", a)

def parse_quantity(value, default=0):
    """Extract numeric quantity from strings like '2 cups', '1.5 kg'."""
    if value is None:
        return default
    s = str(value).strip()
    match = re.search(r"([\d.,]+)", s)
    if match:
        try:
            return float(match.group(1))
        except ValueError:
            pass
    return safe_float(default)

def parse_unit(value, default="units"):
    """Return unit string or a sensible fallback."""
    if not value:
        return default
    u = str(value).strip().lower()
    return u or default
