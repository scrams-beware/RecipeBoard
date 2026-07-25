# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: RecipeBoard
import sys


def handle_keyboard_interrupt():
    """Gracefully exit CLI on Ctrl+C."""
    print("\nRecipeBoard interrupted by user.")
    sys.exit(0)


try:
    while True:
        cmd = input("recipeboard> ")
        if not cmd.strip():
            continue
        if cmd.lower() in ("q", "quit", "exit"):
            handle_keyboard_interrupt()
except KeyboardInterrupt:
    handle_keyboard_interrupt()
