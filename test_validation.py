"""
test_validation.py
Unit tests for pure validation functions in validation.py.
"""

from validation import validate_text, validate_numeric, validate_date, validate_yes_no

# validate_text 
def test_validate_text_valid():
    assert validate_text("John Doe") == True

def test_validate_text_empty():
    assert validate_text("") == False

def test_validate_text_whitespace_only():
    assert validate_text("   ") == False

def test_validate_text_numbers_as_text():
    assert validate_text("123") == False


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


# validate_date

def test_validate_date_valid():
    assert validate_date("12/03/2019") == True

def test_validate_date_wrong_format():
    assert validate_date("2019-03-12") == False

def test_validate_date_invalid_day():
    assert validate_date("32/03/2019") == False

def test_validate_date_empty():
    assert validate_date("") == False

def test_validate_date_text():
    assert validate_date("abc") == False

# validate_yes_no 

def test_validate_yes_no_yes():
    assert validate_yes_no("yes") == True

def test_validate_yes_no_no():
    assert validate_yes_no("no") == True

def test_validate_yes_no_capitalised():
    assert validate_yes_no("Yes") == True

def test_validate_yes_no_invalid():
    assert validate_yes_no("maybe") == False

def test_validate_yes_no_empty():
    assert validate_yes_no("") == False

