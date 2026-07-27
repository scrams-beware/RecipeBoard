# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: RecipeBoard
def format_shopping_list(items: list[ShoppingItem]) -> str:
    """Return a clean, sorted shopping list grouped by category."""
    if not items:
        return "Your shopping list is empty! 🛒"
    groups = {}
    for item in sorted(items, key=lambda x: (x.category or 'Other', x.name.lower())):
        cat = item.category or 'Other'
        groups.setdefault(cat, []).append(item)
    lines = []
    for cat, group in groups.items():
        if len(group) == 1 and group[0].quantity is None:
            lines.append(f"• {group[0].name} ({group[0].unit}) — ${group[0].price:.2f}")
        else:
            total_qty = sum((g.quantity for g in group if g.quantity is not None), start=None)
            line_parts = [f"{g.name}" for g in group]
            if total_qty is not None and any(g.unit for g in group):
                avg_unit = (group[0].unit or "") + f" ({total_qty:.1f})"
            else:
                avg_unit = ""
            lines.append(f"• {cat}: {'; '.join(line_parts)}{avg_unit}")
    return "\n".join(lines)
