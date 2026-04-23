from train_test_split import y_test
from predicting_y import y_pred
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)

print("MSE:", mse)