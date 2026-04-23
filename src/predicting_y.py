from pipeline import pipeline
from train_test_split import X_test

y_pred = pipeline.predict(X_test)

print("Y Prediction:", y_pred)