from sklearn.metrics import (
    mean_absolute_error, mean_squared_error, r2_score
)

def evaluate_reg(model, name, X_test, y_test):
    pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, pred, squared=False)
    mae  = mean_absolute_error(y_test, pred)
    r2   = r2_score(y_test, pred)
    print(f"=== {name} ===\nRMSE={rmse:.3f}  MAE={mae:.3f}  R2={r2:.3f}\n")
    return rmse, mae, r2