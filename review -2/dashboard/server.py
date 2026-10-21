"""Zero-dependency analytics API and web server for the Review 2 case study."""

from __future__ import annotations

import csv
import json
import mimetypes
import os
import statistics
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parent
EXPORTS = ROOT.parent / "dashboard_exports"
STATIC = ROOT / "static"

SEASON_ORDER = ["Spring", "Summer", "Fall", "Winter"]
WEEKDAY_ORDER = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]


def load_csv(name: str) -> list[dict]:
    with (EXPORTS / name).open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    numeric = {
        "hr", "holiday", "workingday", "casual", "registered", "cnt",
        "temp_actual", "atemp_actual", "hum_actual", "wind_actual",
        "Actual_Rentals", "Linear_Regression", "Random_Forest",
        "Gradient_Boosting", "Residual_RF",
    }
    for row in rows:
        for key in numeric & row.keys():
            row[key] = float(row[key])
            if key in {"hr", "holiday", "workingday", "casual", "registered", "cnt"}:
                row[key] = int(row[key])
        if "year_label" in row:
            row["year_label"] = int(row["year_label"])
    return rows


DAILY = load_csv("bike_sharing_daily_processed.csv")
HOURLY = load_csv("bike_sharing_hourly_processed.csv")
PREDICTIONS = load_csv("model_predictions.csv")


QUESTIONS = [
    {"id": 1, "title": "Which season produces the most demand?", "view": "season", "finding": "Fall leads with 5,644 average rentals per day; spring is the low-demand maintenance window at 2,604.", "decision": "Complete heavy fleet maintenance before summer and protect maximum availability through fall."},
    {"id": 2, "title": "How do hourly patterns differ by day type?", "view": "workhour", "finding": "Working days have commuter peaks at 08:00 and 17:00; non-working demand forms a broad midday peak.", "decision": "Use separate weekday and weekend rebalancing schedules."},
    {"id": 3, "title": "How strongly does weather suppress ridership?", "view": "weather", "finding": "Daily demand falls from 4,877 in clear weather to 1,803 in light rain or snow—a 63% reduction.", "decision": "Scale down road rebalancing during adverse weather and move staff to maintenance."},
    {"id": 4, "title": "Did the network grow from 2011 to 2012?", "view": "year", "finding": "Average daily rentals grew 64.4%, from 3,406 to 5,600.", "decision": "Plan capacity expansion; the system is moving from adoption to essential transport infrastructure."},
    {"id": 5, "title": "How do casual and registered riders differ?", "view": "userweekday", "finding": "Registered riders dominate the weekly base while casual participation becomes more prominent on weekends.", "decision": "Target weekend casual riders with conversion offers without reducing commuter capacity."},
    {"id": 6, "title": "What is the temperature–demand relationship?", "view": "temp", "finding": "Temperature and daily rentals have a strong positive correlation (r = 0.627), with demand flattening at hotter ranges.", "decision": "Use temperature bands—not a purely linear rule—in demand planning."},
    {"id": 7, "title": "How does humidity affect demand?", "view": "humidity", "finding": "The daily linear relationship is weakly negative (r = −0.101); humidity alone is not a strong dispatch signal.", "decision": "Treat humidity as a supporting feature alongside temperature and weather condition."},
    {"id": 8, "title": "How does wind speed affect demand?", "view": "wind", "finding": "Wind speed has a modest negative relationship with demand (r = −0.235).", "decision": "Use strong-wind thresholds for safety and small downward demand adjustments."},
    {"id": 9, "title": "What does the 24-month trend reveal?", "view": "timeline", "finding": "Both years repeat a seasonal wave, but 2012 runs at a consistently higher demand level.", "decision": "Separate long-term adoption growth from recurring seasonality in planning."},
    {"id": 10, "title": "Do holidays change total demand?", "view": "holiday", "finding": "Holidays average 3,735 rentals versus 4,527 on non-holidays.", "decision": "Reduce commuter-hour staging on holidays and move capacity toward leisure corridors."},
    {"id": 11, "title": "Which weekdays are busiest?", "view": "weekday", "finding": "Friday leads at 4,690 average daily rentals; Sunday is lowest at 4,229 but has a larger casual share.", "decision": "Protect fleet availability late in the work week and tailor weekend operations to casual users."},
    {"id": 12, "title": "Which hours create operational bottlenecks?", "view": "hour", "finding": "17:00 is the largest system-wide peak at 462 rentals per hour, followed by 18:00 and 08:00.", "decision": "Stage rebalancing crews 30 minutes before the morning and evening peaks."},
    {"id": 13, "title": "Does feels-like temperature add information?", "view": "feel", "finding": "Actual and feels-like temperatures are nearly collinear (r = 0.992).", "decision": "Avoid using both together in a simple linear model; retain feels-like temperature for rider-facing winter messaging."},
    {"id": 14, "title": "Does weather impact change by season?", "view": "seasonweather", "finding": "Adverse-weather demand varies materially across seasons, revealing an interaction that a single weather average hides.", "decision": "Use season-specific weather response rules for staffing and fleet positioning."},
    {"id": 15, "title": "How does the user mix change by season?", "view": "usermix", "finding": "Registered riders provide the stable majority across all seasons; casual share expands during warmer months.", "decision": "Protect subscription service quality while concentrating acquisition campaigns in summer and fall."},
]

HYPOTHESES = [
    {"id": 1, "decision": "2012 demand is higher than 2011", "test": "Welch two-sample t-test", "null": "Mean demand is equal across years", "stat": "t = −15.41", "p": "1.05 × 10⁻⁴⁵", "verdict": "Reject H₀"},
    {"id": 2, "decision": "Weather condition changes demand", "test": "One-way ANOVA", "null": "All weather means are equal", "stat": "F = 65.23", "p": "4.48 × 10⁻²⁶", "verdict": "Reject H₀"},
    {"id": 3, "decision": "Holiday demand differs", "test": "Two-sample t-test", "null": "Holiday and working-day means are equal", "stat": "t = 1.99", "p": "0.0465", "verdict": "Reject H₀"},
    {"id": 4, "decision": "Season changes demand", "test": "One-way ANOVA", "null": "All seasonal means are equal", "stat": "F = 128.77", "p": "6.15 × 10⁻⁶⁷", "verdict": "Reject H₀"},
    {"id": 5, "decision": "Temperature is associated with demand", "test": "Pearson correlation", "null": "ρ(temp, demand) = 0", "stat": "r = +0.627", "p": "2.81 × 10⁻⁸¹", "verdict": "Reject H₀"},
    {"id": 6, "decision": "User mix depends on day type", "test": "Chi-square independence", "null": "User type and day type are independent", "stat": "χ² = 3051.8", "p": "< 1 × 10⁻³⁰⁰", "verdict": "Reject H₀"},
]


def filtered(rows: list[dict], query: dict[str, list[str]], apply_min_demand: bool = True) -> list[dict]:
    year = query.get("year", ["all"])[0]
    season = query.get("season", ["all"])[0]
    weather = query.get("weather", ["all"])[0]
    day_type = query.get("day_type", ["all"])[0]
    date_from = query.get("date_from", [""])[0]
    date_to = query.get("date_to", [""])[0]
    try:
        min_demand = int(query.get("min_demand", ["0"])[0])
    except ValueError:
        min_demand = 0
    output = []
    for row in rows:
        if year != "all" and str(row["year_label"]) != year:
            continue
        if season != "all" and row["season_label"] != season:
            continue
        if weather != "all" and row["weather_label"] != weather:
            continue
        if day_type == "working" and row["workingday"] != 1:
            continue
        if day_type == "off" and row["workingday"] != 0:
            continue
        if date_from and row["dteday"] < date_from:
            continue
        if date_to and row["dteday"] > date_to:
            continue
        if apply_min_demand and row["cnt"] < min_demand:
            continue
        output.append(row)
    return output


def summary(rows: list[dict]) -> dict:
    if not rows:
        return {"records": 0, "total": 0, "daily_average": 0, "registered_share": 0, "peak": None}
    total = sum(row["cnt"] for row in rows)
    peak = max(rows, key=lambda row: row["cnt"])
    return {
        "records": len(rows),
        "total": total,
        "daily_average": round(statistics.mean(row["cnt"] for row in rows), 1),
        "registered_share": round(sum(row["registered"] for row in rows) / total * 100, 1),
        "peak": {"date": peak["dteday"], "rentals": peak["cnt"]},
    }


def model_metrics() -> list[dict]:
    actual = [row["Actual_Rentals"] for row in PREDICTIONS]
    mean_actual = statistics.mean(actual)
    result = []
    for key, label in [("Linear_Regression", "Linear Regression"), ("Random_Forest", "Random Forest"), ("Gradient_Boosting", "Gradient Boosting")]:
        errors = [a - row[key] for a, row in zip(actual, PREDICTIONS)]
        mae = statistics.mean(abs(e) for e in errors)
        rmse = (statistics.mean(e * e for e in errors)) ** 0.5
        r2 = 1 - sum(e * e for e in errors) / sum((a - mean_actual) ** 2 for a in actual)
        result.append({"key": key, "name": label, "r2": round(r2, 4), "mae": round(mae, 1), "rmse": round(rmse, 1)})
    return result


class Handler(BaseHTTPRequestHandler):
    server_version = "CycleScope/1.0"

    def log_message(self, fmt: str, *args) -> None:
        print(f"[dashboard] {self.address_string()} — {fmt % args}")

    def send_json(self, payload, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def send_csv(self, rows: list[dict], filename: str) -> None:
        if not rows:
            return self.send_json({"error": "No rows match the current filters"}, 404)
        from io import StringIO
        stream = StringIO()
        writer = csv.DictWriter(stream, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
        body = stream.getvalue().encode("utf-8-sig")
        self.send_response(200)
        self.send_header("Content-Type", "text/csv; charset=utf-8")
        self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        path = parsed.path
        # Vercel rewrites all API requests to one Python function and forwards
        # the original endpoint in a query parameter.
        if query.get("endpoint"):
            path = "/api/" + query["endpoint"][0].lstrip("/")
        if path == "/api/health":
            return self.send_json({"status": "ok", "daily_rows": len(DAILY), "hourly_rows": len(HOURLY)})
        if path == "/api/meta":
            return self.send_json({"source": "UCI Capital Bikeshare, Washington D.C.", "period": "2011-01-01 to 2012-12-31", "daily_rows": len(DAILY), "hourly_rows": len(HOURLY), "seasons": SEASON_ORDER, "weekdays": WEEKDAY_ORDER})
        if path == "/api/summary":
            return self.send_json(summary(filtered(DAILY, query)))
        if path == "/api/daily":
            return self.send_json(filtered(DAILY, query))
        if path == "/api/hourly":
            return self.send_json(filtered(HOURLY, query, apply_min_demand=False))
        if path == "/api/questions":
            return self.send_json(QUESTIONS)
        if path == "/api/hypotheses":
            return self.send_json(HYPOTHESES)
        if path == "/api/models":
            return self.send_json({"metrics": model_metrics(), "predictions": PREDICTIONS})
        if path == "/api/bi/daily.csv":
            return self.send_csv(filtered(DAILY, query), "bike_sharing_daily_filtered.csv")
        if path == "/api/bi/hourly.csv":
            return self.send_csv(filtered(HOURLY, query, apply_min_demand=False), "bike_sharing_hourly_filtered.csv")
        if path == "/api/bi/predictions.csv":
            return self.send_csv(PREDICTIONS, "model_predictions.csv")
        self.serve_static(path)

    def serve_static(self, request_path: str) -> None:
        relative = "index.html" if request_path in {"", "/"} else request_path.lstrip("/")
        target = (STATIC / relative).resolve()
        try:
            target.relative_to(STATIC.resolve())
        except ValueError:
            return self.send_json({"error": "Invalid path"}, 400)
        if not target.is_file():
            target = STATIC / "index.html"
        body = target.read_bytes()
        content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    host = os.getenv("BIKE_DASH_HOST", "127.0.0.1")
    port = int(os.getenv("BIKE_DASH_PORT", "8000"))
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"CycleScope dashboard: http://{host}:{port}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
