# === Stage 22: Add favorite records and quick favorite listing ===
# Project: RecipeBoard
class FavoriteManager:
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe_id INTEGER UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.db.commit()

    def add_favorite(self, recipe_id: int):
        try:
            self.cursor.execute('INSERT INTO favorites (recipe_id) VALUES (?)', (recipe_id,))
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def remove_favorite(self, recipe_id: int):
        self.cursor.execute('DELETE FROM favorites WHERE recipe_id = ?', (recipe_id,))
        self.db.commit()
        return self.cursor.rowcount > 0

    def is_favorited(self, recipe_id: int) -> bool:
        self.cursor.execute('SELECT COUNT(*) FROM favorites WHERE recipe_id = ?', (recipe_id,))
        return self.cursor.fetchone()[0] > 0

    def get_all_favorite_ids(self):
        self.cursor.execute('SELECT recipe_id FROM favorites ORDER BY created_at DESC')
        return [row[0] for row in self.cursor.fetchall()]

    def close(self):
        self.db.close()
