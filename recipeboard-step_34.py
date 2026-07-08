# === Stage 34: Add support for multiple local user profiles ===
# Project: RecipeBoard
import os
from pathlib import Path

class ProfileManager:
    def __init__(self, base_dir=None):
        self.base = Path(base_dir) if base_dir else Path.home() / ".recipeboard"
        self.profiles_dir = self.base / "profiles"
        self.current_file = None
        self.current_name = None
        self._load_profiles()

    def _load_profiles(self):
        self.profiles = []
        for p in sorted((self.profiles_dir / "*.json").resolve()):
            try:
                with open(p) as f:
                    d = json.load(f)
                name = d.get("name", os.path.basename(p.stem))
                self.profiles.append(Profile(name, Path(str(p))) if not isinstance(d.get("recipes"), list) else Profile.from_dict(name, d))
            except Exception:
                pass

    def set_current(self, profile):
        self.current_file = profile.file
        self.current_name = profile.name
        return self

    def get_current(self):
        return None if not self.current_file else (self.profiles[0] if self.profiles and self.current_file == self.profiles[0].file else Profile.from_file(self.current_file))

    def add_profile(self, name, recipes=None):
        p = Profile(name, Path(self.profiles_dir) / f"{name}.json")
        if recipes:
            for r in recipes:
                p.add_recipe(r)
            with open(p.file) as f:
                data = json.load(f)
            data.setdefault("recipes", [])
            data["recipes"].extend(recipes)
            with open(p.file, "w") as f:
                json.dump(data, f, indent=2)
        return self

    def remove_profile(self):
        if not self.current_file or not os.path.exists(self.current_file):
            return False
        os.remove(self.current_file)
        self.current_file = None
        self.current_name = None
        return True
