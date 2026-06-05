"""
test_validation.py
Unit tests for pure validation functions in validation.py.
"""

from validation import validate_text

# validate_text 
def test_validate_text_valid():
    assert validate_text("John Doe") == True

def test_validate_text_empty():
    assert validate_text("") == False

def test_validate_text_whitespace_only():
    assert validate_text("   ") == False

def test_validate_text_numbers_as_text():
    assert validate_text("123") == True


