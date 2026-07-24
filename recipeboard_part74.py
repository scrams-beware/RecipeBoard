# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: RecipeBoard
def compare_snapshots(before, after):
    """Return a dict describing differences between two state snapshots."""
    changes = {}
    for key in set(list(before.keys()) + list(after.keys())):
        if key in before and key in after:
            if before[key] != after[key]:
                changes[f"{key}_value"] = (before[key], after[key])
        elif key in before:
            changes[f"{key}_removed"] = before[key]
        else:
            changes[f"{key}_added"] = after[key]
    return {**changes, "summary": f"Added: {sum(1 for v in changes.values() if isinstance(v[0], tuple) and v[0][0] is None)}"}
