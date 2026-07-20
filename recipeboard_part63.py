# === Stage 63: Add relationships between records where useful ===
# Project: RecipeBoard
class RecipeBoard:
    def __init__(self):
        self.recipes = []
        self.shopping_lists = []
        self.portions = []
        self.costs = []

    def _find_recipe(self, name):
        return next((r for r in self.recipes if r['name'] == name), None)

    def _find_shopping_list(self, name):
        return next((sl for sl in self.shopping_lists if sl['name'] == name), None)

    def add_ingredients_to_recipe(self, recipe_name, ingredients, portions=None):
        recipe = self._find_recipe(recipe_name)
        if not recipe:
            raise ValueError(f"Recipe '{recipe_name}' not found")
        for ing in ingredients:
            existing = next((i for i in recipe['ingredients'] if i['name'].lower() == ing['name'].lower()), None)
            if existing:
                existing['quantity'] += ing['quantity']
                existing['unit'] = ing['unit']
            else:
                recipe['ingredients'].append(ing.copy())
        return recipe

    def add_shopping_list_item(self, list_name, item):
        sl = self._find_shopping_list(list_name)
        if not sl:
            raise ValueError(f"Shopping list '{list_name}' not found")
        existing = next((i for i in sl['items'] if i['name'].lower() == item['name'].lower()), None)
        if existing:
            existing['quantity'] += item['quantity']
        else:
            sl['items'].append(item.copy())
        return sl

    def link_shopping_list_to_recipe(self, list_name, recipe_names):
        sl = self._find_shopping_list(list_name)
        if not sl:
            raise ValueError(f"Shopping list '{list_name}' not found")
        for rn in recipe_names:
            recipe = self._find_recipe(rn)
            if recipe and recipe['name'] not in [r['name'] for r in sl.get('recipes', [])]:
                sl.setdefault('recipes', []).append(recipe['name'])

    def calculate_total_cost(self, shopping_list_name):
        sl = self._find_shopping_list(shopping_list_name)
        total = 0.0
        if not sl:
            return 0.0
        for item in sl.get('items', []):
            unit_price = self._get_unit_price(item['name']) or 0.0
            total += item['quantity'] * unit_price
        return total

    def _get_unit_price(self, ingredient_name):
        price_map = {r: c for r, c in zip(self.recipes, self.costs)} if self.recipes and self.costs else {}
        return price_map.get(ingredient_name.lower(), 0.0)

    def add_cost_to_recipe(self, recipe_name, total_cost):
        recipe = self._find_recipe(recipe_name)
        if not recipe:
            raise ValueError(f"Recipe '{recipe_name}' not found")
        for i in range(len(self.costs)):
            if self.recipes[i]['name'] == recipe_name:
                self.costs[i] = total_cost
                return
        self.costs.append(total_cost)

    def get_linked_shopping_lists(self, recipe_name):
        linked = []
        for sl in self.shopping_lists:
            recipes_attr = sl.get('recipes', [])
            if recipe_name in recipes_attr:
                linked.append(sl['name'])
        return linked

RecipeBoard.add_relationships = RecipeBoard()
