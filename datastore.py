"""
datastore.py
Contains the DataStore class which handles reading from and
writing to the CSV file.
"""

import pandas as pd
import os
from responses import Response


class DataStore:
    """
    Handles storage of claimant responses to a CSV file.
    """

    def __init__(self, filepath: str = "responses.csv") -> None:
        """
        Initialise the DataStore with a filepath.
        """
        self._filepath = filepath

    @property
    def filepath(self) -> str:
        return self._filepath

    def save(self, response: Response) -> None:
        """
        Save a Response to the CSV file.
        """
        try:
            row = response.to_dict()
            df_new = pd.DataFrame([row])

            if os.path.exists(self._filepath):
                df_new.to_csv(self._filepath, mode='a', header=False, index=False)
            else:
                df_new.to_csv(self._filepath, mode='w', header=True, index=False)

        except Exception as e:
            raise IOError(f"Failed to save response: {e}")

    def load(self) -> pd.DataFrame:
        """
        Load all responses from the CSV file.
        """
        try:
            return pd.read_csv(self._filepath)
        except FileNotFoundError:
            return pd.DataFrame()