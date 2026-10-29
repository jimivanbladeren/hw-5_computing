from abc import ABC, abstractmethod

import pandas as pd


class Preprocessor(ABC):
    """Interface for every preprocessor: `fit` learns from train, `transform` cleans."""

    def fit(self, df_data: pd.DataFrame) -> "Preprocessor":
        """Learn what the preprocessor needs from `df_data`. Nothing by default."""
        return self

    @abstractmethod
    def transform(self, df_data: pd.DataFrame) -> pd.DataFrame:
        pass

    def fit_transform(self, df_data: pd.DataFrame) -> pd.DataFrame:
        return self.fit(df_data).transform(df_data)


class NaNRowsRemover(Preprocessor):
    """Drop the rows that have a NaN in any of `columns`."""

    def __init__(self, columns=("age", "gender", "ethnicity")):
        self._columns = list(columns)

    def transform(self, df_data: pd.DataFrame) -> pd.DataFrame:
        return df_data.dropna(subset=self._columns)


class MeanImputer(Preprocessor):
    """Fill the NaN of each column in `columns` with its mean, learned in `fit`."""

    def __init__(self, columns=("height", "weight")):
        self._columns = list(columns)
        self._means = None

    def fit(self, df_data: pd.DataFrame) -> "MeanImputer":
        self._means = df_data[self._columns].mean()
        return self

    def transform(self, df_data: pd.DataFrame) -> pd.DataFrame:
        if self._means is None:
            raise RuntimeError("Call fit before transform.")
        return df_data.fillna(self._means)
