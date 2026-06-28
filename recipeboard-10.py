# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: RecipeBoard
class SearchFilter:
    def __init__(self, recipes):
        self._recipes = recipes
        self._index = {
            'name': [r['name'].lower() for r in recipes],
            'category': [r.get('category', '').lower() for r in recipes],
            'tags': [[t.lower() for t in r.get('tags', [])] for r in recipes],
        }

    def search(self, query):
        if not query:
            return self._recipes[:]
        q = query.lower().strip()
        results = []
        for i, recipe in enumerate(self._recipes):
            name_match = q in self._index['name'][i]
            cat_match = q in self._index['category'][i] if self._index['category'][i] else False
            tag_matches = any(q in t for t in self._index['tags'][i]) if self._index['tags'][i] else False
            if name_match or cat_match or tag_matches:
                results.append(recipe)
        return results

    def get_index_stats(self):
        total_items = sum(len(v) for v in self._index.values())
        return {'indexed_fields': list(self._index.keys()), 'total_tokens': total_items}
