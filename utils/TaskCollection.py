import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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
