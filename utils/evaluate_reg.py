import os
from sklearn.metrics import (
    mean_absolute_error, root_mean_squared_error, r2_score
)

def evaluate_reg(model, name, X_test, y_test, output_dir):

    pred = model.predict(X_test)
    rmse = root_mean_squared_error(y_test, pred)
    mae  = mean_absolute_error(y_test, pred)
    r2   = r2_score(y_test, pred)

    # Tworzenie raportu
    report_file = os.path.join(output_dir, "task10.md")
    report_lines = []
    report_lines.append(f"=== {name} ===\n")
    report_lines.append(f"RMSE={rmse:.3f}  MAE={mae:.3f}  R2={r2:.3f}\n")
    report_lines.append("\n\n")

    # Zapis raportu do pliku
    with open(report_file, "a", encoding="utf-8") as f:
        f.writelines(report_lines)