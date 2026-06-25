# === Stage 4: Implement create operations for the primary records ===
# Project: RecipeBoard
class RecipeBoardManager:
    def __init__(self, db_file="recipes.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT,
                prep_time_minutes INTEGER,
                servings INTEGER
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe_id INTEGER NOT NULL,
                ingredient_name TEXT NOT NULL,
                quantity REAL NOT NULL,
                unit TEXT NOT NULL,
                cost_per_unit REAL DEFAULT 0.0,
                FOREIGN KEY(recipe_id) REFERENCES recipes(id) ON DELETE CASCADE
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS shopping_list (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ingredient_name TEXT NOT NULL,
                quantity_needed REAL NOT NULL,
                unit TEXT NOT NULL,
                cost_estimate REAL DEFAULT 0.0,
                purchased BOOLEAN DEFAULT FALSE,
                UNIQUE(ingredient_name)
            )
        """)
        self.conn.commit()

    def add_recipe(self, name: str, description: str = "", prep_time: int = 0, servings: int = 1):
        try:
            self.cursor.execute("INSERT INTO recipes (name, description, prep_time_minutes, servings) VALUES (?, ?, ?, ?)",
                               (name, description, prep_time, servings))
            recipe_id = self.cursor.lastrowid
            return recipe_id
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                raise ValueError(f"Recipe '{name}' already exists.") from None
            raise

    def add_ingredient(self, recipe_id: int, ingredient_name: str, quantity: float, unit: str, cost_per_unit: float = 0.0):
        self.cursor.execute("INSERT INTO ingredients (recipe_id, ingredient_name, quantity, unit, cost_per_unit) VALUES (?, ?, ?, ?, ?)",
                           (recipe_id, ingredient_name, quantity, unit, cost_per_unit))
        return self.cursor.lastrowid

    def add_to_shopping_list(self, ingredient_name: str, quantity_needed: float, unit: str):
        try:
            self.cursor.execute("INSERT INTO shopping_list (ingredient_name, quantity_needed, unit) VALUES (?, ?, ?)",
                               (ingredient_name, quantity_needed, unit))
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                raise ValueError(f"Item '{ingredient_name}' already on shopping list.") from None
            raise

    def close(self):
        self.conn.close()
