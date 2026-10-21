# Foundations of Data Science — Coursework Repository
**Course:** 23CSE351 — Foundations of Data Science  
**Student Name:** [Your Name]  
**Register Number:** [Your Register Number]  
**Department:** Computer Science & Engineering  

---

## 📁 Repository Organization

```
D:\fods\
│
├── README.md                                          <-- Repository Overview & Index
│
├── review -1/                                         <-- Lab Evaluation 1 (Risk Analytics)
│   ├── Credit_Card_Risk_Analytics_Master.ipynb        <-- Complete Executed Notebook
│   ├── dataset/
│   │   └── default of credit card clients.xls         <-- Taiwanese Credit Card Dataset
│   └── default_card/
│       └── default of credit card clients.xls         <-- Backward-compatible Dataset
│
└── review -2/                                         <-- Lab Evaluation 2 (Case Study Review)
    ├── Bike_Sharing_Case_Study.ipynb                  <-- Full 10-Section Executed Notebook
    │
    ├── dataset/                                       <-- Clean Dataset Folder
    │   ├── day.csv                                    <-- 731 Daily Aggregated Records
    │   ├── hour.csv                                   <-- 17,379 Hourly Telemetry Records
    │   └── Readme.txt                                 <-- Dataset Documentation
    │
    ├── dashboard_exports/                             <-- Clean Processed Data for BI
    │   ├── bike_sharing_daily_processed.csv           <-- Formatted Daily Data
    │   ├── bike_sharing_hourly_processed.csv          <-- Formatted Hourly Data
    │   └── model_predictions.csv                     <-- ML Predictions vs Actuals
    │
    ├── presentation/                                  <-- 12-Slide Defense Presentation
    │   └── Bike_Sharing_Demand_Case_Study_Presentation.pptx
    │
    └── reports/                                       <-- Academic Case Study Report
        └── Bike_Sharing_Demand_Case_Study_Report.md
```

---

## 📌 Review 1: Credit Card Default Risk Analytics
- **Dataset:** Default of Credit Card Clients (UCI ML Repository, 30,000 customers)
- **Focus:** Data preprocessing, Vector and Matrix operations (customer feature vectors, vector magnitude, Euclidean distance, dot products, covariance/correlation matrix), EDA, Bernoulli/Binomial probability modeling, and empirical Central Limit Theorem (CLT) demonstration.
- **Notebook:** [`review -1/Credit_Card_Risk_Analytics_Master.ipynb`](review%20-1/Credit_Card_Risk_Analytics_Master.ipynb)

---

## 🚲 Review 2: Bike Sharing Demand Analysis & Forecasting
- **Dataset:** Capital Bikeshare System, Washington D.C., USA (UCI ML Repository)
- **Focus:** End-to-end case study featuring:
  1. Data Preprocessing & Denormalization (Physical temperature, humidity, windspeed conversions)
  2. Exploratory Data Analysis answering **15 business and operational questions** with visualizations
  3. Formulated **7 operational decisions** for fleet management and dock rebalancing
  4. **6 Formal Hypothesis Tests** (Welch's $t$-test, One-way ANOVA, Pearson correlation, Chi-square independence)
  5. **Supervised Regression ML Validation** (Random Forest Regressor achieving $R^2 \approx 0.89$, MAE $\approx 439$ bikes)
  6. **Interactive Dashboard Integration:** Power BI & Tableau architecture, live link placeholder, and full-stack backend integration
  7. **Deliverables Included:**
     - Executed Notebook: [`review -2/Bike_Sharing_Case_Study.ipynb`](review%20-2/Bike_Sharing_Case_Study.ipynb)
     - 12-Slide Defense PPT: [`review -2/presentation/Bike_Sharing_Demand_Case_Study_Presentation.pptx`](review%20-2/presentation/Bike_Sharing_Demand_Case_Study_Presentation.pptx)
     - Full Academic Report: [`review -2/reports/Bike_Sharing_Demand_Case_Study_Report.md`](review%20-2/reports/Bike_Sharing_Demand_Case_Study_Report.md)
     - Clean BI Datasets: [`review -2/dashboard_exports/`](review%20-2/dashboard_exports/)
