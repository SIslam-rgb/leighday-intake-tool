"""
test_validation.py
Unit tests for pure validation functions in validation.py.
"""

from validation import validate_text, validate_numeric

# validate_text 
def test_validate_text_valid():
    assert validate_text("John Doe") == True

def test_validate_text_empty():
    assert validate_text("") == False

def test_validate_text_whitespace_only():
    assert validate_text("   ") == False

def test_validate_text_numbers_as_text():
    assert validate_text("123") == True


# validate_numeric

def test_validate_numeric_valid():
    assert validate_numeric("7") == True

def test_validate_numeric_invalid_string():
    assert validate_numeric("abc") == False

def test_validate_numeric_empty():
    assert validate_numeric("") == False

def test_validate_numeric_negative():
    assert validate_numeric("-1") == False

def test_validate_numeric_decimal():
    assert validate_numeric("3.5") == True
    
