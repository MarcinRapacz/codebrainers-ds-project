import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import (
    classification_report, roc_auc_score, roc_curve, confusion_matrix, ConfusionMatrixDisplay,
)

def evaluate_clf(model, name, X_test, y_test, output_dir):
    model_dir = os.path.join(output_dir, name)
    os.makedirs(model_dir, exist_ok=True)
    report_file = os.path.join(output_dir, "task9.md")

    y_pred = model.predict(X_test)
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:,1]
        auc = roc_auc_score(y_test, y_prob)
    else:
        auc = np.nan
        y_prob = None

    # Tworzenie raportu
    report_lines = []
    report_lines.append(f"=== {name} ===\n")
    report_lines.append(f"ROC-AUC: {round(auc, 4)}\n")
    report_lines.append(classification_report(y_test, y_pred, digits=4))
    report_lines.append("\n\n")

    # Zapis raportu do pliku
    with open(report_file, "a", encoding="utf-8") as f:
        f.writelines(report_lines)

    # Macierz pomyłek i zapis wykresu
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    plt.figure()
    disp.plot()
    plt.title(f"Confusion matrix — {name}")
    plt.savefig(os.path.join(model_dir, "confusion_matrix.png"))
    plt.close()

    # Krzywa ROC i zapis wykresu
    if y_prob is not None:
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        plt.figure()
        plt.plot(fpr, tpr)
        plt.plot([0,1],[0,1],'--')
        plt.xlabel("FPR"); plt.ylabel("TPR"); plt.title(f"ROC — {name}")
        plt.savefig(os.path.join(model_dir, "roc_curve.png"))
        plt.close()
