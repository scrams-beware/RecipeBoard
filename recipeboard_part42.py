# === Stage 42: Add CSV export without external dependencies ===
# Project: RecipeBoard
def export_csv(boards, filename="recipeboard.csv"):
    import csv
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for board in boards:
            if isinstance(board, dict):
                writer.writerow(["Board Type:", board.get("name", ""), "Date:", board.get("date", "")])
            elif hasattr(board, "__iter__"):
                writer.writerow([str(b) for b in board[:5]])
    return filename
