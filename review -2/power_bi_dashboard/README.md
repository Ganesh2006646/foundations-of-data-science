# Bike Sharing Power BI Dashboard

Open `Bike_Sharing_Dashboard.pbip` in Power BI Desktop. The project includes:

- 4 completed report pages
- 35 native Power BI visuals
- 23 reusable semantic-model measures
- slicers for year, season, weather, day type, and time period
- EDA, commuter behavior, environmental drivers, and ML evidence pages

The semantic model reads the three public CSV exports from this GitHub repository, so it does not depend on a `D:\...` path from the original computer. On the first refresh, Power BI may ask for data-source credentials; choose **Anonymous** for the public `raw.githubusercontent.com` source.

The committed PBIR files are already generated. If the report layout is intentionally changed in code, rebuild it from this directory with:

```powershell
node build_report.mjs
npx --yes @microsoft/powerbi-report-authoring-cli@latest validate Bike_Sharing_Dashboard.pbip --pretty
```
