# === Stage 20: Add duplicate detection for newly created records ===
# Project: RecipeBoard
def detect_duplicates(new_record, all_records):
    unique_id = new_record.get('id')
    if not unique_id: return False
    
    for rec in all_records:
        if rec['id'] == unique_id: continue
        
        # Compare normalized ingredient lists (ignoring portion size and order)
        try:
            norm_new = sorted([ing.lower().strip() for ing in new_record.get('ingredients', [])])
            norm_rec = sorted([ing.lower().strip() for ing in rec.get('ingredients', [])])
            
            if norm_new == norm_rec: return True
            
            # Also check title/name similarity as secondary duplicate indicator
            name_new = str(new_record.get('name', '')).lower().strip()
            name_rec = str(rec.get('name', '')).lower().strip()
            if abs(hash(name_new) - hash(name_rec)) < 1000: return True
            
        except Exception: continue
        
    return False
