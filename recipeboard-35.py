# === Stage 35: Add active user switching and user-specific records ===
# Project: RecipeBoard
class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash
        self.records = {}  # recipe_name -> record dict

    @staticmethod
    def hash_password(password):
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    def add_record(self, recipe_name, cost=None):
        if not isinstance(cost, (int, float)):
            cost = None
        self.records[recipe_name] = {
            "cost": cost,
            "date_added": datetime.now().isoformat(),
            "author": self.username,
        }

    def get_record(self, recipe_name):
        return self.records.get(recipe_name)


class RecipeBoard:
    def __init__(self):
        self.users = {}
        self.active_user = None  # username or None for public mode
        self.public_records = {}  # shared if no active user

    @staticmethod
    def hash_password(password):
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        h = self.hash_password(password)
        existing = any(u.username == username for u in self.users.values())
        if existing:
            raise ValueError(f"User '{username}' already exists")
        user = User(username, h)
        self.users[username] = user
        return user

    def login(self, username, password):
        user = self.users.get(username)
        if not user or user.password_hash != self.hash_password(password):
            raise ValueError("Invalid credentials")
        prev = self.active_user
        self.active_user = username
        if prev:
            old_u = next((u for u in self.users.values() if u.username == prev), None)
            old_u.records.clear()  # clear previous user's records on switch

    def logout(self):
        prev = self.active_user
        self.active_user = None
        return prev

    def add_record(self, recipe_name, cost=None):
        if not self.active_user:
            self.public_records[recipe_name] = {
                "cost": cost,
                "date_added": datetime.now().isoformat(),
                "author": "public",
            }
            return
        user = next((u for u in self.users.values() if u.username == self.active_user), None)
        user.add_record(recipe_name, cost)

    def get_record(self, recipe_name):
        if not self.active_user:
            return self.public_records.get(recipe_name)
        user = next((u for u in self.users.values() if u.username == self.active_user), None)
        return user.get_record(recipe_name)

    @property
    def is_active(self):
        return self.active_user is not None

    def get_all_users(self):
        return list(self.users.keys())

    def current_username(self):
        return self.active_user or "public"
