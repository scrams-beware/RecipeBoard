# === Stage 25: Add daily summary calculations ===
# Project: RecipeBoard
def calculate_daily_summary(daily_plans):
    total_cost = sum(plan['total_ingredient_cost'] for plan in daily_plans if 'total_ingredient_cost' in plan)
    unique_meals = set()
    for plan in daily_plans:
        if 'meals' in plan and isinstance(plan['meals'], list):
            unique_meals.update(meal.get('name', '') for meal in plan['meals'])
    avg_cost_per_meal = total_cost / len(unique_meals) if unique_meals else 0.0
    return {
        'date': daily_plans[0]['date'] if daily_plans else None,
        'total_spent': round(total_cost, 2),
        'meal_count': len(unique_meals),
        'average_per_meal': round(avg_cost_per_meal, 2)
    }
