# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: RecipeBoard
def score_recipes(self, recipes):
        scores = []
        for r in recipes:
            s = 0
            if self.costs and r['ingredients']:
                total_cost = sum(
                    self._lookup_ingredient_price(r['ingredients'][i]['name'])
                    * (r['portions'] / r['servings'])
                    for i in range(len(r['ingredients']))
                )
                s += 10 - min(total_cost, 3.5)

            if r.get('tags', []):
                popular = {'vegan', 'vegetarian', 'quick', 'easy'}
                s += len(set(r['tags']) & popular) * 2

            if r.get('servings') and r['servings'] <= 4:
                s += 3

            scores.append((r, s))
        return sorted(scores, key=lambda x: -x[1])
