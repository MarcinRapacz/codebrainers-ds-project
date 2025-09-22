import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ast

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MultiLabelBinarizer
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import (
    classification_report, roc_auc_score, roc_curve, confusion_matrix, ConfusionMatrixDisplay,
    mean_absolute_error, mean_squared_error, r2_score, silhouette_score
)
from sklearn.base import BaseEstimator, TransformerMixin

from utils.DataProvider import DataProvider
from utils.TaskCollection import TaskCollection

DATA_PATH = "data.csv"


print("Wersje:")
import sklearn; print("sklearn", sklearn.__version__)
print("pandas", pd.__version__)
print("numpy", np.__version__)

taskCollection = TaskCollection()

data_provider = DataProvider(DATA_PATH)
df = data_provider.get_data()

taskCollection.runAllTasks(df)


print("Wyniki znajduja sie w katalogu out")