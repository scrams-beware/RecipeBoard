# === Stage 16: Add argparse support for the most common commands ===
# Project: RecipeBoard
import argparse

def main():
    parser = argparse.ArgumentParser(description="RecipeBoard CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # List recipes
    list_parser = subparsers.add_parser('list', help='List all recipes')
    list_parser.add_argument('--json', action='store_true', help='Output as JSON')

    # Add recipe
    add_parser = subparsers.add_parser('add', help='Add a new recipe')
    add_parser.add_argument('-n', '--name', required=True, help='Recipe name')
    add_parser.add_argument('-i', '--ingredients', nargs='+', required=True, help='Ingredients list')

    # Calculate cost
    calc_parser = subparsers.add_parser('cost', help='Calculate total cost for a recipe')
    calc_parser.add_argument('recipe_name', help='Name of the recipe to calculate')
    calc_parser.add_argument('-p', '--portions', type=int, default=1, help='Number of portions')

    # Generate shopping list
    shop_parser = subparsers.add_parser('shop', help='Generate shopping list from menu')
    shop_parser.add_argument('--menu', nargs='+', required=True, help='List of recipes to include')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Placeholder for actual logic implementation
    print(f"Command '{args.command}' executed with arguments: {vars(args)}")
    return 0

if __name__ == "__main__":
    exit(main())
