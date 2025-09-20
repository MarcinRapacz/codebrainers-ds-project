import os
import matplotlib.pyplot as plt
import seaborn as sns

class TaskCollection:
    def __init__(self, output_dir="out"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def runTask1(self, df):
        print("---Wykonuje zadanie 1---")
        output_file = os.path.join(self.output_dir, "task1.md")
        with open(output_file, "w", encoding="utf-8") as f:
            print("---Task 1 executed---", file=f)
            print("Shape:", df.shape, file=f)
            print(df.head(10), file=f)
            df.info(buf=f)
            print("---Task 1 completed---", file=f)

    def runTask2(self, df):
        print("---Wykonuje zadanie 2---")
        output_file = os.path.join(self.output_dir, "task2.md")
        with open(output_file, "w", encoding="utf-8") as f:
            print("---Task 2 executed---", file=f)
            df.info(buf=f)
            print("---Task 2 completed---", file=f)

    def runTask3(self, df):
        print("---Wykonuje zadanie 3---")
        output_file = os.path.join(self.output_dir, "task3.md")
        with open(output_file, "w", encoding="utf-8") as f:
            print("---Task 3 executed---", file=f)
            print("Statystyki:", file=f)
            print(df.describe(), file=f)
            print("Danych w Vehicle Type:", file=f)
            print(df["Vehicle Type"].value_counts(), file=f)
            print("Teza: Wartosc transportu wplywa na Vehicle Type", file=f)
            print(df.loc[df["Vehicle Type"].isna(), "Transport"].value_counts(), file=f)
            print("Potwierdzenei tezy: Nan odpowiada transportowi ekologicznemu", file=f)
            print("---Task 3 completed---", file=f)

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