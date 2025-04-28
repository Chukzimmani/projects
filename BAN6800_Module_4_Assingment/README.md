# BAN6800 Module 4 - Business Analytics Model Assignment

This project involves developing a business analytics model to forecast demand using a smart logistics dataset. The objective was to explore, clean, and prepare the data, develop predictive models, evaluate their performance, and recommend the best approach based on business analytics best practices.

---

## Project Structure
```
/BAN6800_Model_4_Assignment/
|
├── data/
│   ├── smart_logistics_dataset.csv         # Raw dataset
│   └── smart_logistics_dataset_cleaned.csv  # Cleaned dataset
|
├── notebooks/
│   ├── BAN6800Module_4_Cleaning_EDA.ipynb    # Data Cleaning and Exploratory Data Analysis
│   └── Module4_Model.ipynb                   # Model Development and Evaluation
|
|
└── README.md                                 # Project Overview
```

---

## Approach

### 1. Data Cleaning and Preparation
- Handled missing values by filling unknown delay reasons.
- Converted Timestamp to datetime format.
- Performed feature engineering (e.g., extracted Month, Day, Efficiency Ratio).
- Encoded categorical variables for modeling.

### 2. Exploratory Data Analysis (EDA)
- Conducted univariate and bivariate analysis to understand data distributions and correlations.
- Visualized important relationships among variables using plots and heatmaps.

### 3. Model Development
- Built two models:
  - **Linear Regression** (Baseline)
  - **Random Forest Regressor** (Advanced)

### 4. Model Evaluation
| Model                  | R² Score | RMSE    |
|:------------------------|:---------|:--------|
| Linear Regression       | 0.6861   | 30.94   |
| Random Forest Regressor | 0.9797   | 7.87    |

- Random Forest significantly outperformed Linear Regression.

### 5. Feature Importance
- Efficiency Ratio and Inventory Level were found to be the most important predictors of demand.

---

## Key Findings
- Operational efficiency (Efficiency Ratio) and inventory management have the greatest impact on demand forecasting.
- Random Forest Regressor should be deployed for future demand forecasting efforts due to its high accuracy.
- Further improvements could include hyperparameter tuning and exploring time series models.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn

---

## How to Run
1. Clone the repository.
2. Navigate to the `/notebooks/` directory.
3. Open the notebooks in JupyterLab, Jupyter Notebook, or Google Colab.
4. Follow the execution cells to reproduce the analysis and modeling.

---

## Author
Chukwudi Ekweani
