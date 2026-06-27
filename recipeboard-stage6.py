# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: RecipeBoard
def delete_recipe(recipe_id: int, confirm_flag: bool = False) -> None:
    if recipe_id in recipes_db:
        if confirm_flag or input(f"Удалить рецепт #{recipe_id}? (y/n): ").lower() == 'y':
            del recipes_db[recipe_id]
            print(f"Рецепт #{recipe_id} удалён.")
        else:
            print("Удаление отменено пользователем.")
    else:
        print(f"Рецепт #{recipe_id} не найден в базе данных.")

def delete_ingredient(recipe_id: int, ingredient_name: str) -> None:
    if recipe_id in recipes_db and ingredient_name in recipes_db[recipe_id]['ingredients']:
        del recipes_db[recipe_id]['ingredients'][ingredient_name]
        print(f"Ингредиент '{ingredient_name}' удалён из рецепта #{recipe_id}.")
    else:
        print("Ошибка: ингредиент не найден или рецепт отсутствует.")

def delete_shopping_item(item_name: str) -> None:
    if item_name in shopping_list:
        del shopping_list[item_name]
        print(f"Позиция '{item_name}' удалена из списка покупок.")
    else:
        print("Ошибка: позиция не найдена в списке покупок.")

def delete_menu_item(menu_day: str, meal_type: str) -> None:
    if menu_day in daily_menu and meal_type in daily_menu[menu_day]:
        del daily_menu[menu_day][meal_type]
        print(f"Блюдо '{daily_menu[menu_day].get(meal_type, '')}' удалено из меню на {menu_day}.")
    else:
        print("Ошибка: блюдо не найдено в меню.")

def delete_cost_record(record_id: int) -> None:
    if record_id in cost_history:
        del cost_history[record_id]
        print(f"Запись о стоимости #{record_id} удалена из истории.")
    else:
        print("Ошибка: запись о стоимости не найдена в истории.")
