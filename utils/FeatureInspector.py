import pandas as pd

class FeatureInspector:
    def __init__(self, df: pd.DataFrame, list_cols=None, target_col="CarbonEmission"):
        if list_cols is None:
            list_cols = []

        self.target_col = target_col  

        self.num_cols = [
            c for c in df.select_dtypes(include="int64").columns
            if c != target_col
        ]
        self.list_cols = list_cols
        self.cat_cols = [
            c for c in df.select_dtypes(include="object").columns
            if c not in list_cols and c != target_col
        ]

    def inspect(self):
        return {
            "num_cols": self.num_cols,
            "cat_cols": self.cat_cols,
            "list_cols": self.list_cols,
        }
