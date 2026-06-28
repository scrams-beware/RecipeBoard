# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: RecipeBoard
from typing import Optional, List, Callable
import re

def filter_recipes(
    recipes: List[dict],
    status_filter: Optional[str] = None,
    category_filter: Optional[str] = None,
    owner_filter: Optional[str] = None,
    tag_filters: Optional[List[str]] = None,
) -> List[dict]:
    """Filter recipe list by optional criteria."""
    if not recipes:
        return []

    def normalize(text: str) -> str:
        return text.lower().strip()

    filtered = recipes
    if status_filter is not None:
        target = normalize(status_filter)
        filtered = [r for r in filtered if normalize(r.get("status", "")) == target]
    if category_filter is not None:
        target = normalize(category_filter)
        filtered = [r for r in filtered if normalize(r.get("category", "")) == target]
    if owner_filter is not None:
        target = normalize(owner_filter)
        filtered = [r for r in filtered if normalize(r.get("owner", "").split(",")[0]) == target]
    if tag_filters is not None:
        tags_lower = {normalize(t): t for t in tag_filters}
        def has_any_tag(recipe: dict) -> bool:
            recipe_tags = [normalize(t) for t in recipe.get("tags", [])]
            return any(tags_lower[t] for t in recipe_tags if t in tags_lower)
        filtered = [r for r in filtered if has_any_tag(r)]

    return filtered
