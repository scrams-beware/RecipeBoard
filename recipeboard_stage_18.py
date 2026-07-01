# === Stage 18: Add an activity log with timestamps and action names ===
# Project: RecipeBoard
from datetime import datetime, timezone
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RecipeBoard")

class ActivityLogger:
    def __init__(self):
        self.log_file = "activity_log.txt"
        self._ensure_header()

    def _ensure_header(self):
        try:
            with open(self.log_file, 'r') as f:
                if not f.readline().startswith("timestamp|action"):
                    raise ValueError("Header missing")
        except FileNotFoundError:
            with open(self.log_file, 'w') as f:
                f.write(f"#{datetime.now(timezone.utc).isoformat()} - RecipeBoard Activity Log\n")
                f.write("# timestamp|action|details\n")

    def log_action(self, action_name: str, details: dict = None):
        try:
            ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            detail_str = json.dumps(details) if details else ""
            line = f"{ts}|{action_name}|{detail_str}\n"
            with open(self.log_file, 'a') as f:
                f.write(line)
        except Exception as e:
            logger.error(f"Failed to write log entry for {action_name}: {e}")

    def get_recent_logs(self, count: int = 10):
        try:
            with open(self.log_file, 'r') as f:
                lines = f.readlines()
                return [line.strip().split('|')[2] if line.startswith('#') else None for line in reversed(lines)][:count]
        except Exception:
            return []

import json
