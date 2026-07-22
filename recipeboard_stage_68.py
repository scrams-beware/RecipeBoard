# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: RecipeBoard
def generate_changelog(activity_log):
    """Generate a compact changelog from an activity log list of dicts."""
    sections = {"Features": [], "Fixes": [], "Improvements": []}
    for entry in activity_log:
        text = (entry.get("description") or "").lower()
        if any(w in text for w in ("add", "new", "create", "introduce")):
            sections["Features"].append(entry.get("title", ""))
        elif any(w in text for w in ("fix", "correct", "patch", "resolve")):
            sections["Fixes"].append(entry.get("title", ""))
        else:
            sections["Improvements"].append(entry.get("title", ""))

    lines = ["CHANGELOG"]
    lines.append("=" * 40)
    for section in ("Features", "Fixes", "Improvements"):
        items = ", ".join(sections[section]) if sections[section] else "none"
        lines.append(f"{section}: {items}")
    return "\n".join(lines)
