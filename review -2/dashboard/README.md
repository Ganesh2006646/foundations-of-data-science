# CycleScope — Review 2 Full-Stack Dashboard

CycleScope is a zero-dependency Python analytics backend with an interactive browser dashboard. It uses the processed Capital Bikeshare files already produced by the Review 2 notebook.

## Run

From the repository root:

```powershell
python "review -2/dashboard/server.py"
```

Open <http://127.0.0.1:8000>.

No package installation is required. The server uses Python's standard library and reads data from `review -2/dashboard_exports/`.

## API and BI integration

| Endpoint | Purpose |
|---|---|
| `/api/health` | Backend and source-row check |
| `/api/summary` | Filter-aware KPI calculation |
| `/api/daily` | Daily JSON data |
| `/api/hourly` | Hourly JSON data |
| `/api/questions` | 15 analysis questions, findings, and decisions |
| `/api/hypotheses` | Six formal test results |
| `/api/models` | Recalculated holdout metrics and predictions |
| `/api/bi/daily.csv` | Power BI/Tableau daily feed |
| `/api/bi/hourly.csv` | Power BI/Tableau hourly feed |
| `/api/bi/predictions.csv` | Model audit feed |

The daily and hourly APIs accept `year`, `season`, `weather`, and `day_type` query parameters. Example:

```text
http://127.0.0.1:8000/api/bi/daily.csv?year=2012&season=Fall
```

In Power BI Desktop, choose **Get Data → Web**, paste an endpoint URL, and select **Load**. In Tableau Desktop, use the text/CSV connector with the downloaded endpoint result or a web-data connector workflow.

When deployed, replace `http://127.0.0.1:8000` with the production Vercel URL. The dashboard automatically displays production endpoint URLs in its BI Bridge section.

## Scope

The application deliberately remains an analysis-led FODS case study. The machine-learning section is a bounded regression benchmark used to validate discovered patterns, not the main project.
