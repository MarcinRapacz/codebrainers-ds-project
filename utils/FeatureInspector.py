import pandas as pd

class FeatureInspector:
    num_cols = []
    cat_cols = []
    list_cols = []

    def __init__(self, df: pd.DataFrame, list_cols=[]):
        self.num_cols = [c for c in df.select_dtypes(include="int64").columns]
        self.list_cols = list_cols
        self.cat_cols = [c for c in df.select_dtypes(include="object").columns if c not in list_cols]

    def inspect(self):
        return {
            "num_cols": self.num_cols,
            "cat_cols": self.cat_cols,
            "list_cols": self.list_cols,
        }