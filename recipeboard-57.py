# === Stage 57: Add structured result objects for command handlers ===
# Project: RecipeBoard
class RecipeResult:
    def __init__(self, status="ok", message="", data=None):
        self.status = status
        self.message = message
        self.data = data

    @staticmethod
    def ok(message=""):
        return RecipeResult(status="ok", message=message)

    @staticmethod
    def error(message=""):
        return RecipeResult(status="error", message=message)

    @staticmethod
    def info(message=""):
        return RecipeResult(status="info", message=message)

    def to_dict(self):
        d = {"status": self.status, "message": self.message}
        if self.data is not None:
            d["data"] = self.data
        return d
