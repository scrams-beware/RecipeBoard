# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: RecipeBoard
def manage_tags(recipe, tags_to_add=None, tags_to_remove=None):
    if recipe.get("tags") is None:
        recipe["tags"] = set()
    for tag in (tags_to_add or []):
        recipe.setdefault("tags", {}).add(tag)
    for tag in (tags_to_remove or []):
        recipe["tags"].discard(tag)

def summarize_by_tags(recipes, active_tag=None):
    if not recipes:
        return {}
    summary = {}
    for r in recipes:
        tags = r.get("tags", set())
        key = active_tag if (active_tag and active_tag in tags) else "all"
        summary.setdefault(key, []).append(r["name"])
    return summary

def get_top_tags(recipes):
    tag_counts = {}
    for r in recipes:
        for t in r.get("tags", set()):
            tag_counts[t] = tag_counts.get(t, 0) + 1
    return sorted(tag_counts.items(), key=lambda x: -x[1])
