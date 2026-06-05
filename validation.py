from datetime import datetime

def validate_text(value: str) -> bool:
    """
    Validate that a value is non-empty text.
    """
    return len(value.strip()) > 0 and all(value.isalpha())

def validate_numeric(value: str) -> bool:
    """Validate that a value is a positive number."""
    try:
        return float(value.strip())>0
    except ValueError:
        return False

def validate_date(value: str) -> bool:
    """
    Validate that a value matches DD/MM/YYYY format.
    """
    try:
        datetime.strptime(value.strip(), "%d/%m/%Y")
        return True
    except ValueError:
        return False
    
def validate_yes_no(value: str) -> bool:
    """
    Validate that a value is yes or no (case insensitive).
    """
    return value.strip().lower() in ["yes", "no"]

