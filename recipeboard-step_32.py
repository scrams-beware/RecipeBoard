# === Stage 32: Add pagination helpers for long console output ===
# Project: RecipeBoard
def paginate(lines, page_size=15):
    """Yield chunks of lines for paginated console display."""
    total = len(lines)
    if total == 0:
        return
    current = 0
    while current < total:
        end = min(current + page_size, total)
        chunk = lines[current:end]
        print(f"\n{'─' * 40}")
        for line in chunk:
            print(line)
        remaining = total - end
        if remaining > 0:
            print(f"Press Enter to continue...")
            input()
        current = end
