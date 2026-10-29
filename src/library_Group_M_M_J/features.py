from abc import ABC, abstractmethod

import pandas as pd


class Feature(ABC):
    """Interface for every feature: `transform` returns the DataFrame with the new columns."""

    @abstractmethod
    def transform(self, df_data: pd.DataFrame) -> pd.DataFrame:
        pass


class DummiesFeature(Feature):
    """One-hot encode `column`, optionally dropping the dummy of `drop_category`."""

    def __init__(self, column: str, drop_category=None):
        self._column = column
        self._drop_category = drop_category

    def transform(self, df_data: pd.DataFrame) -> pd.DataFrame:
        df_out = pd.get_dummies(df_data, columns=[self._column], dtype=int)
        if self._drop_category is not None:
            df_out = df_out.drop(columns=f"{self._column}_{self._drop_category}")
        return df_out


class BinaryFeature(Feature):
    """Add the column `{column}_bin` with `column` recoded through `coding`."""

    def __init__(self, column: str, coding: dict):
        self._column = column
        self._coding = coding

    def transform(self, df_data: pd.DataFrame) -> pd.DataFrame:
        df_out = df_data.copy()
        df_out[f"{self._column}_bin"] = df_out[self._column].map(self._coding)
        return df_out
