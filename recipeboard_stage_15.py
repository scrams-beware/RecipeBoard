# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: RecipeBoard
def dispatch_command(cmd, args):
    commands = {
        "add": lambda a: print(f"Added recipe: {a.get('name')}, cost: {a.get('cost')}"),
        "list": lambda _: print("Available recipes:\n- Pasta (200 RUB)\n- Salad (150 RUB)"),
        "calc": lambda a: print(f"Total for {len(a)} items: {sum(item['price'] * item['qty'] for item in a) if isinstance(a, list) else 'Invalid format'}"),
    }
    action = commands.get(cmd.lower())
    if action:
        return action(args)
    return print(f"Unknown command: {cmd}")
