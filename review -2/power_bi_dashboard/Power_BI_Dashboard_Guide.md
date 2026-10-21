# 📊 Capital Bikeshare Power BI Project (.pbip) — Complete Guide
## Foundations of Data Science — Lab Evaluation 2

This folder contains the complete, native **Power BI Project (.pbip)** for the Capital Bikeshare Demand Analysis case study.

---

## 🚀 How to Open and Use the Dashboard

### Option A: Direct Launch (Recommended)
1. Double-click the file [**`review -2/Open_PowerBI_Dashboard.bat`**](Open_PowerBI_Dashboard.bat).
2. It will automatically detect your installed **Microsoft Power BI Desktop (x64)** and open the [**`Bike_Sharing_Dashboard.pbip`**](Bike_Sharing_Dashboard.pbip) project.

### Option B: Open from Power BI Desktop
1. Launch **Power BI Desktop**.
2. Click **File ▶ Open Report ▶ Browse Reports**.
3. Select [**`Bike_Sharing_Dashboard.pbip`**](Bike_Sharing_Dashboard.pbip).
4. Power BI will read the Semantic Model, load all tables and DAX measures, and present the 4 report pages.

### Option C: Standalone Interactive HTML Preview
1. Double-click [**`Interactive_Dashboard_Preview.html`**](Interactive_Dashboard_Preview.html) to open the interactive dashboard directly in Chrome, Edge, or Firefox.
2. It features live slicers (Year, Season, Working Day), dynamic KPI cards, hourly rush-hour curves, user segmentation donuts, and managerial decision tables!

---

## 📂 Project Structure & Artifacts

| File / Folder | Purpose |
|---|---|
| **`Bike_Sharing_Dashboard.pbip`** | Root entry point for Power BI Desktop. |
| **`Bike_Sharing_Dashboard.Report/`** | Contains visual container definitions, page layouts, and metadata (`report.json`). |
| **`Bike_Sharing_Dashboard.SemanticModel/`** | Contains the Tabular Model TMSL schema (`model.bim`) with M Power Queries and DAX measures. |
| **`DAX_Measures.dax`** | Complete DAX calculations for volume, rush-hour peaks, weather elasticity, and ML error metrics. |
| **`Interactive_Dashboard_Preview.html`** | Standalone interactive web dashboard with slicers and charts. |
| **`dashboard_exports/`** | Pre-processed CSV datasets loaded by the semantic model. |

---

## 📈 Dashboard Pages & Analytical Options

### Page 1: Executive Overview & KPIs
- **Options & Slicers:** Year (2011 vs 2012), Season (Spring to Winter), Day Type (Working Day vs Weekend).
- **KPI Cards:** Total Rentals (3.29M), Daily Mean (4,504), YoY Growth (+64.5%), Registered Share (81.2%).
- **Visuals:** 24-Month Monthly Trend Comparison, Casual vs Registered User Donut.

### Page 2: Commuter vs. Leisure Dynamics
- **Visuals:** 24-Hour Bimodal Peak Curve (Working Days vs Weekends), Rush-Hour Time Period Bar Chart.
- **Insights:** Proves that registered commuters require 30-minute advance dock rebalancing at 8:00 AM and 5:00 PM.

### Page 3: Weather Sensitivity & Environmental Drivers
- **Visuals:** Weather Situation Dampening Chart (Clear vs Mist vs Light Rain vs Heavy Rain), Temperature vs Demand Curve.
- **Insights:** Demonstrates that rain/snow dampens demand by over 60%, justifying indoor maintenance scheduling.

### Page 4: ML Predictions & Scenario Forecasting
- **Visuals:** Actual vs Random Forest Forecasts, Model Residual Distribution.
- **Insights:** Random Forest achieves $R^2 = 0.887$ and MAE = 439.1 bikes, enabling 24-hour advance fleet staging.
