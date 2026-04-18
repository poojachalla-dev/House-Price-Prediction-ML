from sklearn.model_selection import cross_val_score
from pipeline import pipeline
from train_test_split import X_train, y_train

scores = cross_val_score(pipeline, X_train, y_train, cv=5)

print("CV scores:", scores)
print("Mean Score:", scores.mean())