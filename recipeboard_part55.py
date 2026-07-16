# === Stage 55: Add a setting to disable colorized output ===
# Project: RecipeBoard
class ColorSettings:
    """Manages color output settings for RecipeBoard."""

    def __init__(self):
        self.color_enabled = True

    def disable_colors(self, value=True):
        """Enable or disable colorized terminal output."""
        if value:
            import os
            self.color_enabled = False
            os.environ["NO_COLOR"] = "1"
        else:
            self.color_enabled = True

    @property
    def is_color_enabled(self):
        """Return whether colors are currently enabled."""
        return self.color_enabled


# Initialize global color settings
recipe_settings = ColorSettings()
