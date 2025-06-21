# 🌍 Global Health Indicators EDA (2000–2020)

This project explores global health indicators to uncover patterns and relationships between life expectancy, health spending, immunization, and infant mortality. The goal is to extract meaningful insights from WHO data and showcase data science skills relevant to health and development sectors.

## 📌 Project Overview

The project analyzes global health data across multiple countries between 2000 and 2020. The goal is to explore trends in key indicators such as life expectancy, immunization coverage, infant mortality, and health spending — and uncover insights related to global health progress and inequalities.

---

## 🎯 Problem Statement

How have key global health indicators evolved across countries and regions between 2000 and 2020, and what patterns or disparities can be observed?

---

## Dataset
- Source: WHO & UN health indicators (via Kaggle)
- Rows: 2,900+
- Columns: 22 health and economic indicators
- Link: https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who

---

## Objectives
- Understand what affects life expectancy globally
- Compare developed vs. developing countries
- Examine immunization and health spending impact
- Identify countries with high or low health outcomes

---

## EDA and Visualization Steps

1. **Data Loading & Cleaning**
   - Loaded data from GitHub into Colab using pandas
   - Cleaned column names and dropped missing values for some plots

2. **Life Expectancy by Development Status**
   - Compared developed and developing countries using boxplots

3. **Immunization vs. Infant Mortality**
   - Found negative correlation between immunization and infant deaths
   - Visualized with scatter plots and heatmaps

4. **Health Spending vs. Life Expectancy**
   - Higher spending tends to increase life expectancy
   - Some outliers suggest inefficiency or other factors

5. **Trends Over Time**
   - Tracked life expectancy and infant deaths from 2000 to 2015
   - Developing countries show steady improvement

6. **Country Rankings**
   - Top 10 countries by life expectancy
   - Top 10 countries with highest infant mortality

---

## Key Insights

- More immunization is linked to lower infant deaths
- High health spending generally improves life expectancy
- Developing countries are improving but still lag behind
- Outliers show that healthcare quality matters, not just funding

---

## Future Improvements

- Handle missing data with imputation
- Train machine learning models to predict life expectancy
- Build dashboards for country comparisons (Streamlit or Plotly)
- Add per-country reports and interactive charts

---

## How to Run

1. Open the notebook in Google Colab
2. All data loads from a GitHub URL — no upload needed
3. Run cells from top to bottom

---

## Author

- GitHub: https://github.com/yourusername
- Aspiring Data Scientist | Biostatistics | Computer-Aided Drug Discovery
