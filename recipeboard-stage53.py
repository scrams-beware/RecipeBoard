# === Stage 53: Add command help text and usage examples ===
# Project: RecipeBoard
HELP_TEXT = """RecipeBoard — a recipe cost and menu planning board.

Commands:
  show recipes          List all saved recipes with cost summary.
  show shopping         Display the current shopping list grouped by store.
  show costs            Print per-ingredient breakdown and total meal cost.
  add recipe <name>     Add a new recipe (prompted for ingredients and portions).
  remove recipe <name>  Delete a saved recipe.
  plan meals            Plan a multi-meal menu with auto-generated shopping list.
  check budget          Verify total planned cost against your daily budget.
  help                  Show this usage summary."""

EXAMPLES = """Examples:
  python main.py show recipes               # see all recipes and their costs
  python main.py add recipe "Spaghetti"     # interactive ingredient input
  python main.py plan meals                 # auto-plan lunch + dinner menu
  python main.py check budget --budget $50   # stay under $50/day"""
