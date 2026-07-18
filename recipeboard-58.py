# === Stage 58: Add bulk update behavior for selected records ===
# Project: RecipeBoard
from typing import List, Optional


def apply_bulk_update(
    records: dict,
    updates: list,
) -> dict:
    """Apply a list of (record_id, field_name, new_value) tuples to the records dict."""
    for record_id, field_name, new_value in updates:
        if record_id not in records:
            raise KeyError(f"Unknown record id: {record_id!r}")
        records[record_id][field_name] = new_value
    return records


def apply_bulk_update_with_validation(
    records: dict,
    updates: list,
    validators: Optional[List[tuple]] = None,
) -> dict:
    """Bulk update with optional per-field validators.

    Each validator is a (field_name, callable) tuple; the callable takes the new value
    and must return True if acceptable or raise an exception otherwise.
    """
    for record_id, field_name, new_value in updates:
        if record_id not in records:
            raise KeyError(f"Unknown record id: {record_id!r}")
        if validators is not None:
            for v_field, validator_fn in validators:
                if v_field == field_name:
                    validator_fn(new_value)
        records[record_id][field_name] = new_value
    return records


def apply_bulk_update_with_log(
    records: dict,
    updates: list,
    log_fn=None,
) -> dict:
    """Bulk update with an optional side-channel logger."""
    if log_fn is None:
        log_fn = lambda msg: None
    for record_id, field_name, new_value in updates:
        if record_id not in records:
            raise KeyError(f"Unknown record id: {record_id!r}")
        old_val = records[record_id].get(field_name)
        records[record_id][field_name] = new_value
        log_fn(
            f"[bulk-update] {record_id}: {field_name} {old_val!r} -> {new_value!r}"
        )
    return records
