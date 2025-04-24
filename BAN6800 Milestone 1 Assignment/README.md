# Demand Forecasting Using Smart Logistics Data

This project is part of a Business Analytics course and focuses on predicting demand using a real-world-style logistics dataset. The goal is to clean, prepare, and explore the data to build a foundation for future modeling and forecasting.

## 📊 Project Objective

To analyze logistics-related variables and understand demand behavior over time, helping businesses reduce overstocking or understocking through better forecasting.

## 🧾 Dataset Description

- **Source:** Smart Logistics Dataset (Simulated)
- **Rows:** 1,000
- **Columns:** 16
- **Key Features:**
  - Timestamp
  - Inventory Level
  - Demand Forecast
  - Shipment & Traffic Status
  - Temperature & Humidity
  - User Purchase Behavior

## 🛠️ Tools Used

- Python
- Pandas
- Matplotlib & Seaborn (for charts)
- Jupyter Notebook

## 🧹 Data Preparation

- Converted timestamps to proper datetime format
- Removed inconsistencies and missing values
- Created new features:
  - Day of Week, Hour, and Month
  - Efficiency Ratio (Demand ÷ Inventory)
  - Delay Reason Flag
  - Traffic and Inventory Categories

## 📈 Exploratory Data Analysis (EDA)

Key Insights:
- Most demand values are between 150–275 units
- Tuesdays, Thursdays, and Sundays show the highest average demand
- Efficiency Ratio is the strongest predictor of demand
- Weather and waiting time do not have significant impact on demand

## ✅ Deliverables

- `smart_logistics_dataset_cleaned.csv` — Cleaned and processed dataset
- `01_demand_forecasting_data_prep_and_eda.ipynb` — Jupyter notebook with all steps and EDA

## 🚀 Next Steps

- Build predictive models (regression or time series)
- Create dashboards for real-time demand tracking
- Use model insights to recommend inventory planning actions

## 📎 Author

**Chukwudi Ekweani**  
Master’s in Data Analytics (2025)  
GitHub: https://github.com/Chukzimmani  
