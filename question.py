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