# 🌍 Life Expectancy Prediction Using Machine Learning

**A data science project by [@dukejnrs](https://github.com/dukejnrs)**  
Predicting life expectancy from global health, economic, and demographic data.

---

## 📚 Table of Contents

- [📘 Overview](#-overview)
- [📁 Project Structure](#-project-structure)
- [🗃️ Dataset Description](#️-dataset-description)
- [🎯 Objective](#-objective)
- [🔎 Project Workflow](#-project-workflow)
  - [1️⃣ Data Cleaning & Imputation](#1️⃣-data-cleaning--imputation)
  - [2️⃣ Exploratory Data Analysis (EDA)](#2️⃣-exploratory-data-analysis-eda)
  - [3️⃣ Feature Engineering & Scaling](#3️⃣-feature-engineering--scaling)
  - [4️⃣ Modeling & Evaluation](#4️⃣-modeling--evaluation)
  - [5️⃣ Feature Importance](#5️⃣-feature-importance)
- [🧠 Key Insights](#-key-insights)
- [💾 Model File](#-model-file)
- [📈 Results](#-results)
- [🚀 Future Work](#-future-work)
- [👨‍💻 Author](#-author)

---

## 📘 Overview

This project explores global health data to predict **life expectancy** using machine learning models. The process includes:

- End-to-end data preprocessing
- Exploratory data analysis (EDA)
- Feature engineering and scaling
- Model training and evaluation
- Saving the trained model for deployment

---

## 📁 Project Structure

life-expectancy-prediction/ │ ├── notebooks/ │   └── life_expectancy_modeling.ipynb     # Full modeling notebook │ ├── models/ │   └── life_expectancy_rf_model.pkl       # Trained Random Forest model │ ├── data/ │   └── Life_Expectancy_Data.csv           # Raw dataset │ ├── .gitignore                             # Git ignored files └── README.md      # Project documentation

---

---

## 🗃️ Dataset Description

The dataset includes health and development indicators for over 190 countries, such as:

- **Health indicators**: HIV/AIDS prevalence, immunization coverage (Polio, Diphtheria, Hepatitis B), BMI, thinness levels
- **Economic indicators**: Income index, GDP
- **Demographics**: Adult mortality, schooling years
- **Development status**: Developed vs Developing

**Source**: [WHO + UN Health Statistics](https://www.who.int/data)

---

## 🎯 Objective

To build a robust machine learning model that predicts a country’s life expectancy based on key health and socioeconomic factors. This can help policymakers identify high-impact variables that influence longevity.

---

## 🔎 Project Workflow

### 1️⃣ Data Cleaning & Imputation

- Removed duplicates and handled missing values
- Imputed:
  - **Numerical columns**: mean
  - **Categorical/binary columns**: mode or median

### 2️⃣ Exploratory Data Analysis (EDA)

- Visualizations:
  - Distribution of life expectancy by country status
  - Correlation heatmap
  - Relationship plots (e.g. schooling vs life expectancy)
- Outlier detection using boxplots and scatterplots

### 3️⃣ Feature Engineering & Scaling

- **One-hot encoding** of categorical columns like `Status`
- **StandardScaler** for feature scaling
- Removed irrelevant or redundant columns

### 4️⃣ Modeling & Evaluation

- Split data into training and test sets (80:20)
- Models tried:
  - Linear Regression
  - Gradient Boosting Regressor
  - Random Forest Regressor
- **Best model**: Random Forest (after hyperparameter tuning)

#### ✅ Performance Metrics

| Metric        | Value |
|---------------|-------|
| MAE           | 1.07  |
| RMSE          | 1.72  |
| R² Score      | 0.97  |

### 5️⃣ Feature Importance

Top features influencing life expectancy:

- Schooling
- Income composition of resources
- BMI
- Diphtheria immunization
- Polio immunization
- HIV/AIDS prevalence (negative impact)
- Adult mortality (negative impact)
- Thinness (1–19 years) (negative impact)
- Thinness (5–9 years) (negative impact)
- Development status

---

## 🧠 Key Insights

- 📚 Education and economic access are **strongly correlated** with higher life expectancy.
- 🦠 High **HIV/AIDS** prevalence and undernutrition significantly reduce life expectancy.
- 💉 Immunization coverage is **positively correlated** with longevity.
- 🧮 Income composition is a key socioeconomic driver of health outcomes.

---

## 💾 Model File

- ✅ Trained model: [`life_expectancy_rf_model.pkl`](models/life_expectancy_rf_model.pkl)
- 📦 Can be loaded using `joblib.load()` for inference or deployment.

---

## 📈 Results

The tuned Random Forest model achieved **97% accuracy (R²)** on unseen data with minimal error, indicating strong generalization and predictive power.

---

## 🚀 Future Work

- 🧪 Experiment with deep learning or time series modeling
- 🧩 Add external health indicators or longitudinal data
- 🖼 Deploy using Streamlit or Gradio
- 🔍 Perform country-specific feature analysis

---

## 👨‍💻 Author

**Duke Jnrs**  
📍 GitHub: [@dukejnrs](https://github.com/dukejnrs)  
🎓 Aspiring Data Scientist | Interested in Public Health & Biostatistics
