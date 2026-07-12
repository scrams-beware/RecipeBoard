# === Stage 44: Add backup creation for the data file ===
# Project: RecipeBoard
def backup_data_file(data_path, backup_dir="./backups"):
    """Create a timestamped backup of the data file."""
    import shutil
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    src = Path(data_path)
    if not src.exists():
        return False
    dst = Path(backup_dir) / f"{src.name}.{ts}"
    shutil.copy2(src, dst)
    print(f"Backup saved to {dst}")
    return True
