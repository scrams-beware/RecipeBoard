# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: RecipeBoard
def update_recipe_cost(recipe_id, new_ingredients):
    if recipe_id not in recipes:
        print(f"Error: Recipe {recipe_id} not found.")
        return False
    
    for ing_name, qty, price in new_ingredients:
        if (ing_name, price) not in ingredients_db:
            print(f"Warning: Ingredient '{ing_name}' with price {price} is unknown. Skipping.")
            continue
        
        existing = next((i for i in recipes[recipe_id]['ingredients'] if i['name'] == ing_name), None)
        
        if existing:
            old_price = ingredients_db[(ing_name, price)]
            new_total_cost = sum(i['qty'] * i['price'] for i in recipes[recipe_id]['ingredients'])
            
            if abs(new_total_cost - (existing['qty'] * old_price)) < 0.01:
                existing['price'] = price
                existing['qty'] = qty
            else:
                print(f"Warning: Cost mismatch detected for {ing_name}. Keeping original data.")
        else:
            recipes[recipe_id]['ingredients'].append({'name': ing_name, 'qty': qty, 'price': price})
    
    return True
