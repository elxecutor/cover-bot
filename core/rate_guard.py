# rate_guard.py

import time
import json
import os

STATE_FILE = "rate_limit_state.json"
MIN_POST_INTERVAL_SECONDS = 90 * 60  # 90 minutes

def can_post_now() -> bool:
    if not os.path.exists(STATE_FILE):
        return True

    try:
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
            last_ts = data.get("last_post_time", 0)
            return (time.time() - last_ts) >= MIN_POST_INTERVAL_SECONDS
    except Exception:
        return True

def update_last_post_time():
    try:
        with open(STATE_FILE, "w") as f:
            json.dump({"last_post_time": time.time()}, f)
    except Exception as e:
        print(f"⚠️ Failed to update rate state: {e}")
