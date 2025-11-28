import datetime
import random
import string

# ────────────────────────────────────────────────
# GENERATE UNIQUE ID
# ────────────────────────────────────────────────
def generate_id(prefix: str = "ID", length: int = 8) -> str:
    """
    Generates a unique alphanumeric ID with optional prefix.
    """
    suffix = "".join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return f"{prefix}_{suffix}"

# ────────────────────────────────────────────────
# CURRENT TIMESTAMP
# ────────────────────────────────────────────────
def current_timestamp() -> int:
    """
    Returns current UTC timestamp in seconds.
    """
    return int(datetime.datetime.utcnow().timestamp())

# ────────────────────────────────────────────────
# FORMAT DATETIME
# ────────────────────────────────────────────────
def format_datetime(ts: int, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Converts timestamp to formatted string
    """
    return datetime.datetime.utcfromtimestamp(ts).strftime(fmt)

# ────────────────────────────────────────────────
# SAFE DIVIDE
# ────────────────────────────────────────────────
def safe_divide(a: float, b: float, default: float = 0.0) -> float:
    """
    Divides a by b, returns default if b=0
    """
    try:
        return a / b
    except ZeroDivisionError:
        return default
