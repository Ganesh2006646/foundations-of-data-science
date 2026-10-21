# Foundations of Data Science — Coursework Repository
**Course:** 23CSE351 — Foundations of Data Science  
**Student Name:** [Your Name]  
**Register Number:** [Your Register Number]  
**Department:** Computer Science & Engineering  

---

## 🌐 Quick Links & Interactive Dashboards

- **Live Web Dashboard:** [Open CycleScope — Bike Demand Intelligence](https://suhas2006-code.github.io/cycloscope-fods-review-2/)
- **Native Power BI Project:** [`review -2/power_bi_dashboard/Bike_Sharing_Dashboard.pbip`](review%20-2/power_bi_dashboard/Bike_Sharing_Dashboard.pbip)
- **Review 1 Master Notebook:** [`review -1/Credit_Card_Risk_Analytics_Master.ipynb`](review%20-1/Credit_Card_Risk_Analytics_Master.ipynb)
- **Review 2 Master Notebook:** [`review -2/Bike_Sharing_Case_Study.ipynb`](review%20-2/Bike_Sharing_Case_Study.ipynb)
- **Review 2 Academic Report:** [`review -2/reports/Bike_Sharing_Demand_Case_Study_Report.md`](review%20-2/reports/Bike_Sharing_Demand_Case_Study_Report.md)
- **Review 2 Defense Presentation (12 Slides):** [`review -2/presentation/Bike_Sharing_Demand_Case_Study_Presentation.pptx`](review%20-2/presentation/Bike_Sharing_Demand_Case_Study_Presentation.pptx)

---

## 📁 Repository Organization

```text
D:\fods\
│
├── README.md                                          <-- Repository Master Index
├── .gitignore                                         <-- Git Ignore Configuration
│
├── review -1/                                         <-- Lab Evaluation 1 (Credit Card Risk Analytics)
│   ├── README.md                                      <-- Review 1 Overview & Guide
│   ├── Credit_Card_Risk_Analytics_Master.ipynb        <-- Full Executed Master Notebook
│   ├── dataset/
│   │   └── default of credit card clients.xls         <-- Taiwanese Credit Card Dataset (30,000 records)
│   └── default_card/
│       └── default of credit card clients.xls         <-- Compatibility Path Mirror
│
└── review -2/                                         <-- Lab Evaluation 2 (Bike Sharing Case Study)
    ├── Bike_Sharing_Case_Study.ipynb                  <-- Full 10-Section Executed Master Notebook
    │
    ├── dashboard/                                     <-- Full-Stack Web Dashboard (Zero-Dependency Python)
    │   ├── README.md                                  <-- Dashboard API Documentation
    │   ├── server.py                                  <-- Python Standard Library HTTP Server & API
    │   ├── start_dashboard.ps1                        <-- Quick Launch PowerShell Script
    │   └── static/
    │       ├── index.html                             <-- Interactive Frontend Layout
    │       ├── app.js                                 <-- Dashboard Logic, Charts & Slicers
    │       └── styles.css                             <-- Responsive Styling
    │
    ├── power_bi_dashboard/                            <-- Native Power BI Desktop Project (.pbip)
    │   ├── README.md                                  <-- Power BI Architecture & Setup Guide
    │   ├── Bike_Sharing_Dashboard.pbip                <-- Double-Click to Open in Power BI Desktop
    │   ├── Open_PowerBI_Dashboard.bat                 <-- One-Click Auto-Launcher Batch Script
    │   ├── DAX_Measures.dax                           <-- Full DAX Calculation Reference File
    │   ├── build_report.mjs                           <-- PBIR Layout Build Script
    │   ├── Bike_Sharing_Dashboard.Report/             <-- 4 Pages & 35 Native Visual Definitions
    │   └── Bike_Sharing_Dashboard.SemanticModel/      <-- Portable TMSL Schema & M Queries (model.bim)
    │
    ├── dashboard_exports/                             <-- Clean Enriched CSVs Consumed by BI Tools
    │   ├── bike_sharing_daily_processed.csv           <-- 731 Daily Records (Labels, Denormalized Weather)
    │   ├── bike_sharing_hourly_processed.csv          <-- 17,379 Hourly Records (Time Bins, Rush Hours)
    │   └── model_predictions.csv                     <-- ML Predictions (LR, RF, GB vs Actuals)
    │
    ├── dataset/                                       <-- Clean Raw Dataset Folder
    │   ├── day.csv                                    <-- Daily Aggregated Data
    │   ├── hour.csv                                   <-- Hourly Telemetry Data
    │   └── Readme.txt                                 <-- Official Dataset Documentation & Attribution
    │
    ├── presentation/                                  <-- 12-Slide Evaluation Defense Deck (16:9 Widescreen)
    │   └── Bike_Sharing_Demand_Case_Study_Presentation.pptx
    │
    └── reports/                                       <-- Comprehensive Academic Case Study Report
        └── Bike_Sharing_Demand_Case_Study_Report.md
```

---

## 📌 Review 1: Credit Card Default Risk Analytics

- **Dataset:** Default of Credit Card Clients (UCI Machine Learning Repository, 30,000 customers)
- **Key Focus Areas:**
  - **Data Preprocessing:** Null/duplicate checks, category repair, Label Encoding, `StandardScaler`, and PCA dimensionality reduction.
  - **Linear Algebra & Vector Concepts:** Customer feature vectors, average vector difference ($ec{X}_{yes} - ec{X}_{no}$), vector magnitude, Euclidean distance, dot products, covariance, and correlation matrices.
  - **Exploratory Data Analysis:** 15 focused analytical questions answered with clear visualizations and plain-English interpretations.
  - **Probability Distributions:** Independence test using the multiplication rule, conditional probability risk curves, and Binomial distribution ($n=10, p=0.2212$).
  - **Sampling & Central Limit Theorem (CLT):** Margin of error tables across sample sizes ($n \in [50, 5000]$), sample size requirement calculations, and $2 	imes 2$ subplot histograms demonstrating normal distribution emergence.
- **Master Notebook:** [`review -1/Credit_Card_Risk_Analytics_Master.ipynb`](review%20-1/Credit_Card_Risk_Analytics_Master.ipynb)

---

## 🚲 Review 2: Bike Sharing Demand Analysis & Predictive Forecasting

- **Dataset:** Capital Bikeshare System, Washington D.C., USA (UCI Machine Learning Repository, 17,379 hourly / 731 daily records)
- **Key Methodological Deliverables:**
  1. **Data Preprocessing & Denormalization:** Restored normalized weather features to physical units (°C, %, km/h) and created operational rush-hour bins.
  2. **15 Business & Operational Questions:** Each answered with code, dedicated visualizations, and operational justifications.
  3. **7 Strategic Operational Decisions:** Formulated clear decisions on fleet expansion, 30-minute advance dock rebalancing, and weather-adaptive scheduling.
  4. **6 Formal Hypothesis Tests (8 Marks Rubric):**
     - Welch's Two-Sample $t$-test (2011 vs. 2012 ridership growth: $+64.5\%$, $p < 0.001$)
     - One-way ANOVA (Weather condition impact: $F = 65.23, p < 0.001$)
     - Two-sample $t$-test (Holidays vs. Working days: $p = 0.0465$)
     - One-way ANOVA (Seasonality: $F = 128.77, p < 0.001$)
     - Pearson Correlation Significance (Temperature vs. Demand: $r = +0.627, p < 0.001$)
     - Chi-square Test of Independence (User type vs. Day type: $\chi^2 = 3051.8, p < 0.001$)
  5. **Supervised Regression ML Validation (7 Marks Rubric):**
     - Compared Linear Regression, Ridge, Random Forest Regressor, and Gradient Boosting.
     - Justified Random Forest as the optimal non-linear model ($R^2 \approx 0.887$, MAE $\approx 439$ bikes/day).
     - Confirmed that this is an analysis-led project using ML as a validation engine.
  6. **Native Power BI Project (`.pbip`):**
     - 4 completed pages (Executive Overview, Commuter Dynamics, Weather Sensitivity, ML Forecasts).
     - 35 native visuals and 23 DAX measures.
     - Portable data model powered by public web CSV sources.
  7. **Full-Stack Web Dashboard & API:**
     - Zero-dependency Python server exposing dynamic REST endpoints and real-time interactive analytics.

---

## 🚀 Quickstart Guides

### 1. Launch the Full-Stack Web Dashboard
Run the Python backend server from the repository root:
```powershell
python "review -2/dashboard/server.py"
```
Open [**http://127.0.0.1:8000**](http://127.0.0.1:8000) in your web browser.

### 2. Open the Native Power BI Project
Double-click [**`review -2/power_bi_dashboard/Open_PowerBI_Dashboard.bat`**](review%20-2/power_bi_dashboard/Open_PowerBI_Dashboard.bat) or open [**`review -2/power_bi_dashboard/Bike_Sharing_Dashboard.pbip`**](review%20-2/power_bi_dashboard/Bike_Sharing_Dashboard.pbip) directly in Microsoft Power BI Desktop.

### 3. Review the Presentation and Academic Report
- Open the 16:9 defense presentation: [`review -2/presentation/Bike_Sharing_Demand_Case_Study_Presentation.pptx`](review%20-2/presentation/Bike_Sharing_Demand_Case_Study_Presentation.pptx)
- Read the full academic case study report: [`review -2/reports/Bike_Sharing_Demand_Case_Study_Report.md`](review%20-2/reports/Bike_Sharing_Demand_Case_Study_Report.md)
