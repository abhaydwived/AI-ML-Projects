# Customer Churn Prediction

## Overview

This project analyzes customer churn using machine learning models. The workflow includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, and evaluation.

## Steps

1. Data Preprocessing: Handle missing values, encode categorical features, normalize numerical data.

2. EDA: Identify trends, correlations, and patterns.

3. Feature Engineering: Create new features like purchase frequency and loyalty score.

4. Model Training: Train Logistic Regression, Random Forest, and XGBoost models.

5. Evaluation: Assess models using Precision-Recall and ROC-AUC metrics.

6. Insights: Identify key churn factors and provide recommendations.

## Requirements

Python

Pandas, NumPy, Matplotlib, Seaborn

Scikit-learn, XGBoost

## Usage

Run the script to preprocess data, visualize insights, train models, and evaluate performance. Modify hyperparameters for better results.

## Results

Key Factors: Days since last purchase, customer satisfaction, total purchases.

Model Performance:

Logistic Regression: ROC-AUC score: 54%

Random Forest: ROC-AUC score: 48%

XGBoost: ROC-AUC score: 78% (Best performing model)


