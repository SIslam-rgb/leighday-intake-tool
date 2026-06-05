from datetime import datetime

def validate_text(value: str) -> bool:
    """
    Validate that a value is non-empty text.
    """
    return len(value.strip()) > 0

def validate_numeric(value: str) -> bool:
    """Validate that a value is a positive number."""
    try:
        float(value.strip())>0
        return True
    except ValueError:
        return False
