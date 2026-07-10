# === Stage 41: Add plain text import for a simple line-based format ===
# Project: RecipeBoard
def parse_plain_text(text: str) -> dict:
    """Parse a simple line-based plain text format into structured data."""
    result = {}
    for line in text.strip().splitlines():
        if not line or line.startswith('#'):
            continue
        parts = [p.strip() for p in line.split(':')]
        if len(parts) == 2:
            key, value = parts
            if key.isidentifier():
                result[key] = value.strip('""''')
    return result

def format_plain_text(data: dict) -> str:
    """Convert structured data back to plain text line-based format."""
    lines = []
    for key in sorted(data.keys()):
        lines.append(f"{key}:{data[key]}")
    return '\n'.join(lines) + '\n'

if __name__ == "__main__":
    sample_input = '''# Recipe Name: Pasta Carbonara
Course:Dinner
Difficulty:Medium
PrepTime:15 minutes
Servings:4'''

    parsed = parse_plain_text(sample_input)
    print("Parsed:", parsed)

    formatted = format_plain_text(parsed)
    print("Formatted:\n", formatted)
