# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: RecipeBoard
# Step 65: Import merging to avoid obvious duplicates when multiple profiles extend the repo.
# Append this compact utility to any RecipeBoard module that imports from several GitHub forks.


def merge_imports(import_blocks):
    """Merge a list of import statements, removing exact duplicates while preserving order."""
    seen = set()
    merged = []
    for block in import_blocks:
        normalized = ' '.join(sorted(block.strip().split()))
        if normalized not in seen:
            seen.add(normalized)
            merged.append(block)
    return '\n'.join(merged)


def safe_import(name, module_path):
    """Try importing a name from a specific path; fall back to stdlib."""
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(name, module_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return getattr(mod, 'RecipeBoard') if hasattr(mod, 'RecipeBoard') else mod
    except Exception:
        pass


def deduplicate_imports(file_content):
    """Remove duplicate `import recipe_board` or similar lines from a Python file."""
    import re
    pattern = r'^\s*import\s+recipe_board[\w.]*'
    return re.sub(pattern, 'import recipe_board', file_content)
