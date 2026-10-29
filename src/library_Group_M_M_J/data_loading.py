from abc import ABC, abstractmethod

import pandas as pd
from sklearn import model_selection


def load_data(path) -> pd.DataFrame:
    """Read a CSV file into a DataFrame."""
    return pd.read_csv(path)


def split_data(df_data, test_size=0.2, random_state=42):
    """Split `df_data` into train and test DataFrames."""
    return model_selection.train_test_split(
        df_data, test_size=test_size, random_state=random_state
    )


class Reader(ABC):
    """Interface for every reader: `read` returns the train and test DataFrames."""

    @abstractmethod
    def read(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        pass


class CSVReader(Reader):
    """Read a CSV file and split it into train and test."""

    def __init__(self, path, test_size=0.2, random_state=42):
        self._path = path
        self._test_size = test_size
        self._random_state = random_state

    def read(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        df_data = load_data(self._path)
        df_train, df_test = split_data(df_data, self._test_size, self._random_state)
        return df_train, df_test
