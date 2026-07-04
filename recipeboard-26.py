# === Stage 26: Add weekly summary calculations ===
# Project: RecipeBoard
def calculate_weekly_summary(weekly_plans, ingredient_costs):
    total_spent = 0.0
    meals_count = 0
    for day in weekly_plans:
        if day.get('meals'):
            for meal in day['meals']:
                cost = sum(meal['ingredients'].get(name, {}).get('cost', 0) * quantity 
                          for name, quantity in meal['ingredients'].items())
                total_spent += cost
                meals_count += 1
    avg_cost_per_meal = total_spent / meals_count if meals_count > 0 else 0.0
    return {'total_weekly_cost': round(total_spent, 2), 'meals_served': meals_count, 
            'average_cost_per_meal': round(avg_cost_per_meal, 2)}
