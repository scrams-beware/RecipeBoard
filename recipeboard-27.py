# === Stage 27: Add monthly summary calculations ===
# Project: RecipeBoard
def calculate_monthly_summary(records):
    from collections import defaultdict
    month_costs = defaultdict(float)
    ingredient_totals = defaultdict(lambda: {'count': 0, 'cost': 0.0})
    for r in records:
        if not isinstance(r.get('date'), str): continue
        try:
            year_month = r['date'][:7]
            month_costs[year_month] += float(r.get('total_cost', 0))
            ing = r.get('ingredients', []) or []
            for item in ing:
                name, qty, price = item.get('name'), item.get('qty'), item.get('price')
                if not all([name, str(price).replace('.', '').isdigit()]): continue
                cost = float(str(price).replace(',', '.')) * (item.get('unit', 1) or 1)
                ingredient_totals[name]['count'] += 1
                ingredient_totals[name]['cost'] += cost
        except Exception:
            pass
    sorted_months = sorted(month_costs.items(), key=lambda x: x[0], reverse=True)[:3]
    top_ingredients = sorted(ingredient_totals.items(), key=lambda x: x[1]['count'], reverse=True)[:5]
    return {
        'top_spending_months': [{'month': m, 'cost': c} for m, c in sorted_months],
        'most_used_ingredients': [{'name': n, 'times_used': i['count'], 'total_cost': round(i['cost'], 2)} for n, i in top_ingredients]
    }
