import numpy as np
import pandas as pd
import ast
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.base import BaseEstimator, TransformerMixin

class ListToMLB(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.mlb_ = MultiLabelBinarizer()

    @staticmethod
    def _parse_cell(x):
        if isinstance(x, list):
            return x
        if isinstance(x, float) and pd.isna(x):
            return []
        if isinstance(x, str):
            s = x.strip()
            if s.startswith('[') and s.endswith(']'):
                try:
                    return ast.literal_eval(s)
                except Exception:
                    return []
            return []
        return []
    
    # def fit(self, X, y=None):
    #     col = pd.Series(X.ravel()).apply(self._parse_cell)
    #     self.mlb_.fit(col)
    #     return self

    # def transform(self, X):
    #     col = pd.Series(X.ravel()).apply(self._parse_cell)
    #     return self.mlb_.transform(col)

    def fit(self, X, y=None):
        if isinstance(X, pd.DataFrame):
            X = X.iloc[:, 0]
        col = X.apply(self._parse_cell)
        self.mlb_.fit(col)
        return self

    def transform(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.iloc[:, 0]
        col = X.apply(self._parse_cell)
        return self.mlb_.transform(col)

    def get_feature_names_out(self, input_features=None):
        return np.array([f"list__{c}" for c in self.mlb_.classes_], dtype=object)
