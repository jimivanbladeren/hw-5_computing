from abc import ABC, abstractmethod

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


class Model(ABC):
    """Interface for every model: `train` fits it, `predict` returns probabilities."""

    def __init__(self, features: list[str], target: str, hyperparameters=None):
        self._features = features
        self._target = target
        self._hyperparameters = hyperparameters or {}

    @abstractmethod
    def train(self, df_train: pd.DataFrame) -> None:
        pass

    @abstractmethod
    def predict(self, df_data: pd.DataFrame) -> np.ndarray:
        pass


class LogisticRegressionModel(Model):
    """Logistic regression on `features` to predict `target`."""

    def __init__(self, features: list[str], target: str, hyperparameters=None):
        super().__init__(features, target, hyperparameters)
        self.model = LogisticRegression(**{"max_iter": 1000, **self._hyperparameters})

    def train(self, df_train: pd.DataFrame) -> None:
        self.model.fit(df_train[self._features], df_train[self._target])

    def predict(self, df_data: pd.DataFrame) -> np.ndarray:
        """Probability of the positive class (target = 1) for each row."""
        return self.model.predict_proba(df_data[self._features])[:, 1]
