from train_test_split import y_train, y_test
from sklearn.metrics import mean_squared_error
from Calculating_Root_Mean_Square_Error import rmse
import numpy as np

baseline = y_train.mean()
baseline_preds = [baseline] * len(y_test)

baseline_mse = mean_squared_error(y_test, baseline_preds)
baseline_rmse = np.sqrt(baseline_mse)

print("Baseline RMSE:", baseline_rmse)
print("Linear Regression:", rmse)