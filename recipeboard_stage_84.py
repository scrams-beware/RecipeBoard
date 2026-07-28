# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: RecipeBoard
def _clean_unused_helpers():
    """Remove duplicate and unused utility functions from RecipeBoard."""
    import inspect, re
    source = open("recipe_board.py", "r").read()
    lines = source.split("\n")
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if (stripped.startswith("def _unused_helper") or
            stripped.startswith("def _deprecated_") or
            stripped.startswith("# TODO: remove later")):
            continue
        if stripped and not stripped.startswith("#"):
            cleaned.append(line)
    return "\n".join(cleaned)

RecipeBoard_source = _clean_unused_helpers()
open("recipe_board.py", "w").write(RecipeBoard_source)
print("Cleanup complete.")
