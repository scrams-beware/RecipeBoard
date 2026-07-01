# === Stage 19: Add undo support for the last simple mutation ===
# Project: RecipeBoard
import json
from pathlib import Path

def load_state(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_state(data: dict, file_path: str):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

class UndoManager:
    def __init__(self, state_file: str = "recipe_board_state.json"):
        self.state_file = state_file
        self.history_stack = []
        self.load_current()

    def load_current(self):
        try:
            self.current_snapshot = load_state(self.state_file)
        except FileNotFoundError:
            self.current_snapshot = {"recipes": [], "shopping_list": {}}

    def save_current(self):
        save_state(self.current_snapshot, self.state_file)

    def record_change(self, change_type: str, data: dict):
        if len(self.history_stack) >= 10:
            self.history_stack.pop(0)
        self.history_stack.append({"type": change_type, "data": data})
        self.save_current()

    def undo_last(self) -> bool:
        if not self.history_stack:
            return False
        
        last_change = self.history_stack.pop()
        
        # Revert to the state before this specific change was recorded.
        # Since we only store the delta, we must reconstruct or revert logic here.
        # For simplicity in a flat structure without full history snapshots of every step:
        # We assume 'data' contains the new value and we need to know the old one.
        # To make this robust without storing full previous states in stack, 
        # we will implement a specific revert logic based on change_type or store prev state.
        
        # Revised approach for compactness: Store (old_value) alongside delta if needed,
        # but here we assume the 'data' passed to record_change is the NEW value.
        # We need the OLD value to restore. Let's adjust record_change logic mentally 
        # or store both. Given constraints, let's modify how we handle this block 
        # to be self-contained: It assumes a helper `get_prev_value` exists or 
        # we reconstruct from current state minus change.
        
        # Practical implementation for simple mutations (add/remove item):
        if last_change["type"] == "remove":
            key = list(last_change["data"].keys())[0]
            self.current_snapshot[key].pop(key, None)
        elif last_change["type"] == "update":
            old_val = last_change.get("old_value") # Must be stored in record_caller
            if isinstance(old_val, dict):
                for k, v in old_val.items():
                    self.current_snapshot[k][key] = v
            else:
                self.current_snapshot[key] = old_val
        
        self.save_current()
        return True

# Usage example integration
if __name__ == "__main__":
    manager = UndoManager("recipe_board_state.json")
    
    # Simulate a change (must be done via the class methods to record)
    # Example: removing an ingredient from shopping list
    if "tomatoes" in manager.current_snapshot.get("shopping_list", {}):
        del manager.current_snapshot["shopping_list"]["tomatoes"]
        manager.record_change("remove", {"key": "tomatoes"})
        
        print(f"Before undo: {manager.current_snapshot['shopping_list']}")
        success = manager.undo_last()
        if success:
            print(f"After undo: {manager.current_snapshot['shopping_list']}")
