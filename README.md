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
├── README.md                                          <-- Repository Master Index
│
├── review -1/                                         <-- Lab Evaluation 1 (Credit Card Risk Analytics)
│   ├── Credit_Card_Risk_Analytics_Master.ipynb        <-- Complete Executed Student-Friendly Notebook
│   ├── dataset/
│   │   └── default of credit card clients.xls         <-- Credit Card Default Dataset (30,000 clients)
│   └── default_card/
│       └── default of credit card clients.xls         <-- Compatibility Dataset Mirror
│
└── review -2/                                         <-- Lab Evaluation 2 (Bike Sharing Demand Case Study)
    ├── Bike_Sharing_Case_Study.ipynb                  <-- Full 10-Section Executed Master Notebook
    │
    ├── dataset/                                       <-- Raw Dataset Records
    │   ├── day.csv                                    <-- 731 Daily Aggregated Records
    │   ├── hour.csv                                   <-- 17,379 Hourly Telemetry Records
    │   └── Readme.txt                                 <-- Dataset Source & Schema Documentation
    │
    ├── dashboard_exports/                             <-- Clean Enriched Data for Power BI / Tableau
    │   ├── bike_sharing_daily_processed.csv           <-- Processed Daily Metrics
    │   ├── bike_sharing_hourly_processed.csv          <-- Processed Hourly Metrics & Time Periods
    │   └── model_predictions.csv                     <-- ML Predictions (LR, RF, GB vs Actuals)
    │
    ├── power_bi_dashboard/                            <-- Native Power BI Desktop Project (.pbip)
    │   ├── Bike_Sharing_Dashboard.pbip                <-- Double-Click to Open in Power BI Desktop
    │   ├── Open_PowerBI_Dashboard.bat                 <-- One-Click Auto-Launcher Batch Script
    │   ├── Bike_Sharing_Dashboard.Report/             <-- Visuals, Pages & Themes (report.json)
    │   ├── Bike_Sharing_Dashboard.SemanticModel/      <-- TMSL Model Schema, M Queries (model.bim)
    │   ├── DAX_Measures.dax                           <-- Full DAX Calculation Reference File
    │   ├── Interactive_Dashboard_Preview.html         <-- Standalone Browser Dashboard with Live Slicers
    │   └── Power_BI_Dashboard_Guide.md               <-- Step-by-Step User & Presentation Guide
    │
    ├── presentation/                                  <-- 12-Slide Evaluation Defense Deck (16:9)
    │   └── Bike_Sharing_Demand_Case_Study_Presentation.pptx
    │
    └── reports/                                       <-- Comprehensive Academic Case Study Report
        └── Bike_Sharing_Demand_Case_Study_Report.md
```

---

## 📌 Review 1: Credit Card Default Risk Analytics
- **Dataset:** Default of Credit Card Clients (UCI ML Repository, 30,000 customers)
- **Topics Covered:** Data preprocessing, Vector and Matrix operations (feature vectors, vector magnitude, Euclidean distance, dot products, covariance/correlation matrix), EDA, Bernoulli/Binomial probability distributions, and Central Limit Theorem (CLT) demonstration.
- **Notebook:** [`review -1/Credit_Card_Risk_Analytics_Master.ipynb`](review%20-1/Credit_Card_Risk_Analytics_Master.ipynb)

---

## 🚲 Review 2: Bike Sharing Demand Analysis & Forecasting
- **Dataset:** Capital Bikeshare System, Washington D.C., USA (UCI ML Repository)
- **Topics Covered:**
  1. Data Preprocessing & Denormalization (Physical units for temperature, humidity, and wind velocity)
  2. Exploratory Data Analysis answering **15 business questions** with visualizations
  3. Formulated **7 operational decisions** for fleet allocation and dock rebalancing
  4. **6 Formal Hypothesis Tests** (Welch's $t$-test, One-way ANOVA, Pearson correlation, Chi-square test of independence)
  5. **Supervised Regression ML Validation** (Random Forest Regressor achieving $R^2 \approx 0.89$, MAE $\approx 439$ bikes)
  6. **Interactive Power BI Dashboard Project (`.pbip`):** Native project with semantic data model, DAX measures, batch launcher, and standalone HTML preview
  7. **Deliverables:**
     - Notebook: [`review -2/Bike_Sharing_Case_Study.ipynb`](review%20-2/Bike_Sharing_Case_Study.ipynb)
     - Power BI Project: [`review -2/power_bi_dashboard/`](review%20-2/power_bi_dashboard/)
     - Presentation PPT: [`review -2/presentation/Bike_Sharing_Demand_Case_Study_Presentation.pptx`](review%20-2/presentation/Bike_Sharing_Demand_Case_Study_Presentation.pptx)
     - Report: [`review -2/reports/Bike_Sharing_Demand_Case_Study_Report.md`](review%20-2/reports/Bike_Sharing_Demand_Case_Study_Report.md)
