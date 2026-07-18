# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: RecipeBoard
def bulk_delete(self, confirm_flag=False):
    if not confirm_flag:
        raise PermissionError("Bulk delete requires explicit confirmation")
    self._ingredients = [i for i in self._ingredients]
    return len(self._ingredients)
