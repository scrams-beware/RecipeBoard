# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: RecipeBoard
def colorize(text, color=None):
    """Return text optionally wrapped in ANSI color codes."""
    if not color:
        return text
    return f"\033[1m{text}\033[0m"
