# 🌍 Life Expectancy Prediction Using Machine Learning

A data science project by [@dukejnrs](https://github.com/dukejnrs)

This project explores global health data to **predict life expectancy** using various machine learning models. The work includes full data cleaning, exploratory data analysis (EDA), feature engineering, modeling, and interpretation.

---

## 📁 Dataset
The dataset contains information on:
- Immunization coverage (Polio, Hepatitis B, Diphtheria)
- Economic indicators (GDP, income index)
- Health indicators (BMI, HIV/AIDS, thinness levels)
- Education (schooling years)
- Development status (Developed vs Developing countries)
- And more...

Source: WHO + UN Health Statistics  
(Used via `Life_Expectancy_Data.csv` on [Google Colab](https://colab.research.google.com))

---

## 🎯 Objective
To build a robust machine learning model that predicts a country's **life expectancy** based on health, economic, and demographic factors. The goal is to gain insights that can inform health policy decisions.

---

## 🔎 Project Steps

### 1. Data Cleaning & Imputation
- Identified missing values across key features
- Imputed:
  - Numeric columns with **mean**
  - Categorical/binary columns with **mode/median**

### 2. Exploratory Data Analysis (EDA)
- Visualized:
  - Life expectancy by development status
  - Immunization coverage and its impact
  - Correlation between variables
- Detected and discussed outliers

### 3. Feature Engineering & Scaling
- One-hot encoded categorical columns (e.g., `Status`)
- Scaled features using `StandardScaler`

### 4. Modeling
- **Train-test split** (80:20)
- Evaluated 3 regression models:
  - **Linear Regression**
  - **Random Forest Regressor**
  - **Gradient Boosting Regressor**

#### ✅ Best Model: Tuned Random Forest
| Metric | Value |
|--------|--------|
| MAE (Mean Absolute Error) | **1.07** |
| RMSE (Root Mean Squared Error) | **1.72** |
| R² Score | **0.97** |

---

## 🔍 Feature Importance

Top 10 features driving life expectancy:
1. **Schooling**
2. **Income Composition of Resources**
3. **BMI**
4. **Diphtheria Immunization**
5. **Polio Immunization**
6. **Adult Mortality** (negative impact)
7. **HIV/AIDS Prevalence** (negative impact)
8. **Thinness (1-19 years)** (negative impact)
9. **Thinness (5-9 years)** (negative impact)
10. **Status (Developing)** (negative impact)

---

## 🧠 Insights
- Better education and economic access **strongly improve** life expectancy.
- High HIV/AIDS prevalence and undernutrition **drastically reduce** life expectancy.
- Immunization programs correlate positively with longevity.

---

## ✅ Next Steps
- [ ] Save and deploy the model
- [ ] Create an interactive dashboard (Streamlit/Gradio)
- [ ] Try deep learning or time-series approaches
- [ ] Add more health indicators (if available)

---

## 👨‍💻 Author
**Duke Jnrs**  
[GitHub Profile »](https://github.com/dukejnrs)

---
