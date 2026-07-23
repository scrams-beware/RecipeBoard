# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: RecipeBoard
class RecipeBoard:
    def __init__(self):
        self._board = {"recipes": {}, "shopping_list": []}
        self.confirm_clear = False

    def clear_board(self):
        if not self.confirm_clear:
            raise PermissionError("Confirm clearing the board first.")
        self._board["recipes"] = {}
        self._board["shopping_list"] = []
        self.confirm_clear = False
