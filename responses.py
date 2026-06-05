"""
response.py
Contains the Response class which holds a single claimant's
complete answers alongside session metadata.
"""

from datetime import datetime

class Response:
    """
    Holds a single claimant's complete answers and session metadata.

    Attributes:
        _session_meta (dict): Case reference, associate name, interview date.
        _answers (dict): Claimant's answers keyed by question label.
        _timestamp (str): The datetime the response was submitted.
    """

    def __init__(self, session_meta: dict, answers: dict) -> None:
        """initialise a Response instance."""
        self._session_meta = session_meta
        self._answers = answers
        self._timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

    @property
    def session_meta(self) -> dict:
        """Return the session metadata."""
        return self._session_meta

    @property
    def answers(self) -> dict:
        """Return the claimant answers."""
        return self._answers

    @property
    def timestamp(self) -> str:
        """Return the submission timestamp."""
        return self._timestamp

    def to_dict(self) -> dict:
        """
        Convert the response to a flat dictionary for CSV export.Returns a flat dictionary combining metadata, answers and timestamp.
        """
        row = {}
        row["timestamp"] = self._timestamp
        row["case_ref"] = self._session_meta.get("case_ref", "")
        row["associate_name"] = self._session_meta.get("associate_name", "")
        row["interview_date"] = self._session_meta.get("interview_date", "")
        row.update(self._answers)
        return row