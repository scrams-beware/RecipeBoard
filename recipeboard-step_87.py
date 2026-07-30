# === Stage 87: Add small helper functions for comparing two exported reports ===
# Project: RecipeBoard
def compare_reports(report_a, report_b):
    """Compare two exported reports and return a summary of differences."""
    if isinstance(report_a, dict) and isinstance(report_b, dict):
        common_keys = set(report_a.keys()) & set(report_b.keys())
        differences = []
        for key in sorted(common_keys):
            val_a = report_a.get(key)
            val_b = report_b.get(key)
            if val_a != val_b:
                differences.append(f"{key}: {val_a} -> {val_b}")
    elif isinstance(report_a, list) and isinstance(report_b, list):
        if len(report_a) != len(report_b):
            return "Reports have different lengths"
        for i in range(len(report_a)):
            if report_a[i] != report_b[i]:
                differences.append(f"Item {i}: {report_a[i]} -> {report_b[i]}")
    else:
        differences = ["Unsupported report type"]
    
    return "Identical" if not differences else "; ".join(differences)

def check_cost_consistency(recipe_report, shopping_list):
    """Verify that the total cost in a recipe report matches the shopping list."""
    total_shopping_cost = sum(item.get("cost", 0) for item in shopping_list if isinstance(item, dict))
    return "Consistent" if abs(total_shopping_cost - recipe_report.get("total_cost", float('inf'))) < 1 else f"Mismatch: expected {recipe_report.get('total_cost')}, got {total_shopping_cost}"
