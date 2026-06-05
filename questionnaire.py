"""
questionnaire.py
Contains the Questionnaire class which manages the ordered list
of questions for the Leigh Day claimant intake session.
"""

from question import Question, TextQuestion, NumericQuestion, DateQuestion, YesNoQuestion

class Questionnaire:
    """
    Manages the ordered list of questions for the claimant intake session.
    
    Attributes:
        _questions (list): The list of Question objects.
    """

    def __init__(self) -> None:
        """Initialise the Questionnaire with the intake questions."""
        self._questions = [
            TextQuestion("What is the claimant's full name?"),
            TextQuestion("What is the claimant's home village or region?"),
            NumericQuestion("How many years were you employed at the site?"),
            DateQuestion("What was the date of the first incident? (DD/MM/YYYY)"),
            YesNoQuestion("Were you provided with any protective equipment? (yes/no)"),
        ]

    @property
    def questions(self) -> list:
        """Return the list of questions."""
        return self._questions

    def get_question(self, index: int) -> Question:
        """
        Return a question by index.
        """
        return self._questions[index]

    def total_questions(self) -> int:
        """
        Return the total number of questions.
        """
        return len(self._questions)

    def is_complete(self, answers: dict) -> bool:
        """
        Check whether all required questions have been answered.
        """
        for question in self._questions:
            if question.required and question.label not in answers:
                return False
        return True