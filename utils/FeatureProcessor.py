
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from utils.ListToMLB import ListToMLB
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

class FeatureProcessor:
    def __init__(self, list_cols, num_cols, cat_cols):
        self.preprocess = self._build_preprocess(
            list_cols=list_cols, 
            num_cols=num_cols,
            cat_cols=cat_cols
        )

    def _build_preprocess(self, list_cols, num_cols, cat_cols):
        num_pipe = Pipeline([
            ("scaler", StandardScaler())
        ])

        cat_cols_special = ["Vehicle Type"]
        cat_cols_other = [c for c in cat_cols if c != "Vehicle Type"]

        vehicle_pipe = Pipeline([
            ("imputer", SimpleImputer(strategy="constant", fill_value="Eco")),
            ("encoder", OneHotEncoder())
        ])

        cat_pipe = Pipeline([
            ("encoder", OneHotEncoder())
        ])

        list_transforms = [
            (f'list_{i}', Pipeline([
                ('list', ListToMLB()),
            ]), [col]) for i, col in enumerate(list_cols)
        ]
        preprocess = ColumnTransformer(
            transformers=[
                ('num', num_pipe, num_cols),
                ('cat-other', cat_pipe, cat_cols_other),
                ('cat-vehicle', vehicle_pipe, cat_cols_special),
                *list_transforms
            ],
            remainder='drop'
        )

        return preprocess