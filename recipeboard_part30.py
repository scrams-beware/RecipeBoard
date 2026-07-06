# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: RecipeBoard
def parse_date(date_str):
    """Parse a date string in DD/MM/YYYY, YYYY-MM-DD, or YYYY/MM/DD format. Returns a datetime.date object."""
    from datetime import date
    if not isinstance(date_str, str) or len(date_str.strip()) == 0:
        raise ValueError("Date string is empty or invalid.")

    cleaned = date_str.strip()
    
    # Try DD/MM/YYYY first (common in recipes and Europe)
    parts = cleaned.split('/')
    if len(parts) == 3:
        day, month, year = [int(p) for p in parts]
        try:
            return date(year, month, day)
        except ValueError as e:
            raise ValueError(f"Invalid DD/MM/YYYY date '{cleaned}': {e}")

    # Try YYYY-MM-DD (ISO standard)
    parts = cleaned.split('-')
    if len(parts) == 3:
        year, month, day = [int(p) for p in parts]
        try:
            return date(year, month, day)
        except ValueError as e:
            raise ValueError(f"Invalid YYYY-MM-DD date '{cleaned}': {e}")

    # Try YYYY/MM/DD (ambiguous but valid)
    parts = cleaned.split('/')
    if len(parts) == 3:
        year, month, day = [int(p) for p in parts]
        try:
            return date(year, month, day)
        except ValueError as e:
            raise ValueError(f"Invalid YYYY/MM/DD date '{cleaned}': {e}")

    raise ValueError(f"Date string '{date_str}' is not recognized. Use formats like DD/MM/YYYY or YYYY-MM-DD.")
