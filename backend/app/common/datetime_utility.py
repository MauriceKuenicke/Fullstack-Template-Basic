from datetime import datetime, timezone

def get_current_ts_string() -> str:
    """
    Retrieve the current UTC timestamp as a string in ISO 8601-like format.

    :return: Current timestamp in the format 'YYYY-MM-DD HH:MM:SS.ffffff'.
    """
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')