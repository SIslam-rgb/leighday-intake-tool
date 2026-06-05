from validation import validate_text, validate_numeric, validate_date, validate_yes_no
"""
Create a blue print for questions
"""

class Question:
    """
    parent class representing a single intake questionnaire question.

    Attributes:
        _label (str): The question text displayed to the user.
        _field_type (str): The expected input type.
        _required (bool): Whether an answer is required.
    """
    def __init__(self,label:str,field_type: str,required: bool = True) -> None:
        self._label = label
        self._field_type = field_type
        self._required = required

    @property
    def label(self) -> str:
        """Return the question label."""
        return self._label

    @property
    def field_type(self) -> str:
        """Return the field type."""
        return self._field_type

    @property
    def required(self) -> bool:
        """Return whether the question is required."""
        return self._required
    
class TextQuestion(Question):
    """A question that expects a plain text response."""
    def __init__(self, label: str, required: bool = True) -> None:
        super().__init__(label, "text", required)

    def validate(self, value: str) -> bool:
        return validate_text(value)
    
class NumericQuestion(Question):
    """A question that expects a positive number response."""
    def __init__(self, label: str, required: bool = True) -> None:
        super().__init__(label, "numeric", required)

    def validate(self, value: str) -> bool:
        return validate_numeric(value)

class DateQuestion(Question):
    """A question that expects a date response d/m/y."""
    def __init__(self, label: str, required: bool = True) -> None:
        super().__init__(label, "date", required)

    def validate(self, value: str) -> bool:
        return validate_date(value)
    
class YesNoQuestion(Question):
    """A question that expects a yes no."""
    def __init__(self, label: str, required: bool = True) -> None:
        super().__init__(label, "yes_no", required)

    def validate(self, value: str) -> bool:
        return validate_yes_no(value)