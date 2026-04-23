# 🏠 House Price Prediction using Machine Learning

## 📌 Overview

This project builds an end-to-end machine learning pipeline to predict house prices using structured data. It starts with a simple baseline, progresses through linear modeling, and improves performance using ensemble methods and hyperparameter tuning.

---

## 🎯 Objectives

* Build a regression model to predict house prices
* Establish a baseline for performance comparison
* Implement a clean and reusable ML pipeline
* Improve performance using advanced models and tuning

---

## 📊 Dataset

* Source: Kaggle House Prices Dataset
* Records: 1460
* Features: 80+
* Target: `SalePrice`

---

## 🔍 Features Used

* `GrLivArea` – Above-ground living area
* `BedroomAbvGr` – Number of bedrooms
* `FullBath` – Number of bathrooms

These features were selected for their strong correlation with house prices.

---

## ⚙️ Workflow

1. Data Loading & Exploration
2. Feature Selection
3. Train-Test Split
4. Preprocessing (Imputation + Scaling)
5. Model Training
6. Evaluation & Baseline Comparison
7. Model Improvement (Random Forest + Tuning)

---

## 🧠 Models Used

### 1. Baseline Model

* Strategy: Predict mean house price
* Purpose: Establish minimum performance benchmark

### 2. Linear Regression

* Simple and interpretable model
* Built using a pipeline (imputer + scaler + model)

### 3. Random Forest Regressor

* Captures non-linear relationships
* Tuned using GridSearchCV

---

## 📈 Results

| Model                 | RMSE   |
| --------------------- | ------ |
| Baseline              | 87,619 |
| Linear Regression     | 52,975 |
| Random Forest (Tuned) | 47,374 |

✅ ~40% improvement over baseline (Linear Regression)

🚀 ~46% improvement over baseline (Random Forest)

---

## 🔁 Cross-Validation

* 5-fold cross-validation used
* Mean score: **0.556**
* Ensures model stability and avoids overfitting

---

## 📊 Visualizations

* Actual vs Predicted plots
* Model comparison plots
* Error distribution (boxplot)

These visualizations help evaluate prediction quality and model performance.

---

## 💡 Key Insights

* Baseline comparison is critical to validate model usefulness
* Linear models provide strong starting points
* Ensemble models significantly improve performance
* Hyperparameter tuning leads to better generalization
* Pipelines prevent data leakage and ensure consistency

---

## 🛠️ Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🚀 Future Improvements

* Use more features for better accuracy
* Try Gradient Boosting / XGBoost
* Perform feature engineering
* Deploy model using Flask or Streamlit

---

## 📎 Conclusion

This project demonstrates a complete machine learning workflow, from baseline modeling to advanced model tuning. The results highlight how model selection and optimization significantly improve predictive performance.

---

## 📬 Contact

Feel free to connect for feedback or collaboration!
