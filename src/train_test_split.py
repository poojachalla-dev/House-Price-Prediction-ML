from select_input_features_and_target_variable import X, y
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 42
)

print(f"X.shape = {X.shape}")
print(f"X_train.shape = {X_train.shape}")
print(f"X_test.shape = {X_test.shape}")

print(f"y_train.shape = {y_train.shape}")
print(f"y_test.shape = {y_test.shape}")

print(X_train.head())
print(X_test.head())