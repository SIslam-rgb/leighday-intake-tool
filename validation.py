from datetime import datetime

def validate_text(value: str) -> bool:
    """
    Validate that a value is non-empty text.
    """
    return len(value.strip()) > 0
