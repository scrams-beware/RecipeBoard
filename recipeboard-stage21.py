# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: RecipeBoard
import json, os, shutil
ARCHIVE_DIR = "archive"
def archive_record(record_id):
    if record_id in records:
        path = f"{ARCHIVE_DIR}/{record_id}.json"
        try:
            with open(path, 'w') as f:
                json.dump(records[record_id], f)
        except Exception: pass
        del records[record_id]

def restore_record(record_id):
    if record_id in records or not os.path.exists(f"{ARCHIVE_DIR}/{record_id}.json"): return False
    try:
        with open(f"{ARCHIVE_DIR}/{record_id}.json") as f:
            data = json.load(f)
        records[record_id] = data
        shutil.rmtree(ARCHIVE_DIR, ignore_errors=True)
        os.makedirs(ARCHIVE_DIR)
        return True
    except Exception: return False
