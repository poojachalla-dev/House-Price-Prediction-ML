# 🏠 House Price Prediction using Machine Learning

## 📌 Overview

This project focuses on building a machine learning model to predict house prices based on key features such as living area, number of bedrooms, and number of bathrooms. The goal is to understand how simple models perform and to evaluate their effectiveness against a baseline.

---

## 🎯 Objectives

* Build a regression model to predict house prices
* Implement a clean and reproducible ML pipeline
* Compare model performance with a baseline approach
* Evaluate model reliability using cross-validation

---

## 📊 Dataset

* Source: Kaggle House Prices Dataset
* Total Records: 1460
* Features: 80+
* Target Variable: `SalePrice`

---

## 🔍 Feature Selection

Selected key features based on domain intuition:

* `GrLivArea` – Above-ground living area
* `BedroomAbvGr` – Number of bedrooms
* `FullBath` – Number of full bathrooms

---

## ⚙️ Workflow

1. Data Loading and Exploration
2. Feature Selection
3. Train-Test Split
4. Data Preprocessing

   * Missing value imputation
   * Feature scaling
5. Model Training
6. Model Evaluation
7. Baseline Comparison

---

## 🧠 Model Pipeline

A machine learning pipeline was used to ensure consistency and avoid data leakage:

* **Imputer**: Handles missing values using mean strategy
* **Scaler**: Standardizes numerical features
* **Model**: Linear Regression

---

## 📈 Evaluation Metrics

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Cross-validation score (cv=5)

---

## 📊 Results

| Model             | RMSE   |
| ----------------- | ------ |
| Baseline (Mean)   | 87,619 |
| Linear Regression | 52,975 |

✅ Achieved ~40% reduction in error compared to baseline

---

## 🔁 Cross-Validation

* Performed 5-fold cross-validation
* Mean score: **0.556**
* Ensures model stability and reliability

---

## 💡 Key Insights

* Even simple models can perform well with meaningful features
* Baseline comparison is essential to validate model usefulness
* Pipelines help prevent data leakage and improve reproducibility

---

## 🛠️ Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

## 📎 Conclusion

This project demonstrates a complete machine learning workflow, from data preprocessing to model evaluation. The model significantly outperforms the baseline, indicating that the selected features provide meaningful predictive power.

---

## 📬 Contact

If you have any feedback or suggestions, feel free to connect!
