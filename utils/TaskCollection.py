import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

from utils.FeatureInspector import FeatureInspector
from utils.FeatureProcessor import FeatureProcessor
from utils.evaluate_reg import evaluate_reg
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from utils.evaluate_clf import evaluate_clf


class TaskCollection:
    def __init__(self, output_dir="out"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def runTask1(self, df):
        print("---Wykonuje zadanie 1---")
        output_file = os.path.join(self.output_dir, "task1.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Task 1 Report\n\n")
            
            f.write("## Kształt danych\n")
            f.write(f"Liczba wierszy i kolumn: {df.shape}\n\n")
            
            f.write("## Pierwsze 10 wierszy\n")
            f.write("```\n")
            f.write(df.head(10).to_string(index=False))
            f.write("\n```\n\n")
            
            f.write("## Informacje o kolumnach\n")
            f.write("```\n")
            df.info(buf=f)
            f.write("\n```\n\n")
            
            f.write("## Statystyki opisowe (kolumny numeryczne)\n")
            f.write("```\n")
            f.write(df.describe().to_string())
            f.write("\n```\n\n")

    def runTask2(self, df):
        print("---Wykonuje zadanie 2---")
        output_file = os.path.join(self.output_dir, "task2.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Task 2 Report\n\n")
            
            f.write("## Informacje o kolumnach\n")
            f.write("```\n")
            df.info(buf=f)
            f.write("\n```\n\n")

    def runTask3(self, df):
        print("---Wykonuje zadanie 3---")
        output_file = os.path.join(self.output_dir, "task3.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Task 3 Report\n\n")
            
            f.write("## Statystyki opisowe wszystkich kolumn numerycznych\n")
            f.write("```\n")
            f.write(df.describe().to_string())
            f.write("\n```\n\n")
            
            f.write("## Wartości w kolumnie Vehicle Type\n")
            f.write("```\n")
            f.write(df["Vehicle Type"].value_counts().to_string())
            f.write("\n```\n\n")
            
            f.write("## Teza: Wartość transportu wpływa na Vehicle Type\n")
            f.write("```\n")
            f.write(df.loc[df["Vehicle Type"].isna(), "Transport"].value_counts().to_string())
            f.write("\n```\n\n")

    def runTask4(self, df):
        print("---Generuje wykresy do zadania 4---")
        # Histogramy
        plt.figure(figsize=(12, 8))
        df.hist()
        plt.suptitle("Histogramy zmiennych")
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "histograms.png"))
        plt.close()

        # Boxploty
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df)
        plt.xticks(rotation=45)
        plt.title("Boxplot wszystkich zmiennych")
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "boxplot.png"))
        plt.close()

        # Scatter matrix (pairplot)
        pairplot = sns.pairplot(df, diag_kind="kde")
        pairplot.fig.suptitle("Scatter matrix", y=1.02)
        pairplot.savefig(os.path.join(self.output_dir, "scatter_matrix.png"))
        plt.close()

        # Heatmapa korelacji (tylko zmienne numeryczne)
        df_num = df.select_dtypes(include=["int64"])
        plt.figure(figsize=(10, 6))
        sns.heatmap(df_num.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Macierz korelacji (tylko zmienne numeryczne)")
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "correlation_heatmap.png"))
        plt.close()

    def runTask5(self, df):
        print("---Skip zadanie 5---")
        # Zgodnie z instrukcją, zadanie 5 nie jest wymagane do implementacji.

    def runTask6(self, df):
        print("---Wykonuje zadanie 6---")
        feature_inspector = FeatureInspector(df, list_cols=["Recycling", "Cooking_With"])
        output_file = os.path.join(self.output_dir, "task6.md")
        data = feature_inspector.inspect();

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Task 6 Report\n\n")
            f.write("## Rodzaje kolumn\n")
            f.write("```\n")
            f.write(json.dumps(data, indent=2, ensure_ascii=False))
            f.write("\n```\n\n")

        return data

    def runTask7(self, columns):
        print("---Wykonuje zadanie 7---")
        return FeatureProcessor(
            list_cols=columns['list_cols'], 
            num_cols=columns['num_cols'],
            cat_cols=columns['cat_cols']
        )
    
    def runTask8(self, df):
        print("---Wykonuje zadanie 8---")
        
        # Ta część jest już stworzona i wypełniona, nie musisz nic zmieniac. Tworzy ona etykietę binarną bazując na kwantylu emisji (np. górny kwartyl) do celów klasyfikacji.
        q = 0.8
        y_reg = df['CarbonEmission'].copy()
        thr = y_reg.quantile(q)
        y_clf = (y_reg >= thr).astype(int)

        X = df.drop(columns=['CarbonEmission'])
        print("Próg emisji:", thr, " | Udział klasy 1:", y_clf.mean().round(3))

        output_file = os.path.join(self.output_dir, "task8.md")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Task 8 Report\n\n")
            f.write("```\n")
            f.write(f"X: {X}\n")
            f.write(f"y_reg: {y_reg}\n")
            f.write(f"y_clf: {y_clf}\n")
            f.write(f"thr: {thr}\n")
            f.write("```\n\n")

        return X, y_reg, y_clf, thr
    
    def runTask9(self, processor: FeatureProcessor, X, y_reg, y_clf, thr):
        print("---Wykonuje zadanie 9---")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_clf, test_size=0.2, random_state=42, stratify=y_clf
        )

        pipe_knn = Pipeline([
            ("preprocess", processor.preprocess),
            ("knn", KNeighborsClassifier())
        ])

        param_knn = {
            "knn__n_neighbors": [3, 5, 7, 9],
            "knn__weights": ["uniform", "distance"]
        }

        gs_knn = GridSearchCV(
            estimator=pipe_knn,
            param_grid=param_knn,
            cv=5,
            scoring="f1",
        )

        gs_knn.fit(X_train, y_train)
        evaluate_clf(gs_knn.best_estimator_, "task9 - KNN (best)", X_test, y_test, self.output_dir)


        pipe_lr = Pipeline([
            ("preprocess", processor.preprocess),
            ("lr", LogisticRegression(random_state=42, max_iter=2000, n_jobs=-1))
        ])

        param_lr = {
            "lr__C": [0.01, 0.1, 1, 10],
            "lr__solver": ["lbfgs", "saga"]
        }

        gs_lr = GridSearchCV(
            estimator=pipe_lr,
            param_grid=param_lr,
            cv=5,
            scoring='f1',
            n_jobs=-1,
            verbose=1
        )

        gs_lr.fit(X_train, y_train)
        evaluate_clf(gs_lr.best_estimator_, "task9 - LogisticRegression (best)", X_test, y_test, self.output_dir)

    # def runTask10(self, df: pd.DataFrame, preprocess: FeatureProcessor):
    #     print("---Wykonuje zadanie 10---")
    #     y = df['CarbonEmission'].copy()
    #     X = df.drop(columns=['CarbonEmission'])

    #     X_train, X_test, y_train, y_test = #TODO: podziel dane na zbiór treningowy i testowy (np. test_size=0.2, random_state=42)

    #     pipe_knnr = None #TODO: stwórz pipeline z preprocess i KNeighborsRegressor
    #     param_knnr = None #TODO: zdefiniuj parametry do strojenia
    #     gs_knnr = None #TODO: uzupełnij GridSearchCV z pipe_knnr i param_knnr
    #     gs_knnr.fit(X_train, y_train)

    #     pipe_lin = Pipeline([('prep', preprocess), ('reg', LinearRegression())])
    #     pipe_lin.fit(X_train, y_train)

        

    #     evaluate_reg(gs_knnr.best_estimator_, "KNNRegressor (best)", X_test, y_test)
    #     evaluate_reg(pipe_lin, "LinearRegression", X_test, y_test)


    def runAllTasks(self, df: pd.DataFrame):
        self.runTask1(df)
        self.runTask2(df)
        self.runTask3(df)
        self.runTask4(df)
        self.runTask5(df)
        columns = self.runTask6(df)
        feature_processor = self.runTask7(columns)
        X, y_reg, y_clf, thr = self.runTask8(df)
        self.runTask9(feature_processor, X, y_reg, y_clf, thr)
        # self.runTask10(df, feature_processor)