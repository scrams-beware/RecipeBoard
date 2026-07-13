# === Stage 46: Add a schema version field and migration helper ===
# Project: RecipeBoard
SCHEMA_VERSION = 46


def migrate_to_v46(data: dict) -> dict:
    """Upgrade a RecipeBoard config to schema v46.

    Adds the ``schema_version`` field and ensures the default value is set.
    Returns the updated configuration dictionary unchanged otherwise.
    """
    if "schema_version" not in data or data["schema_version"] < 46:
        data.setdefault("schema_version", 46)
        return data
    return data
