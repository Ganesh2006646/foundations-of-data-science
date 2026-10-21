"""Build the dependency-free GitHub Pages edition into /docs."""

from __future__ import annotations

import importlib.util
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DASHBOARD = ROOT / "review -2" / "dashboard"
STATIC = DASHBOARD / "static"
EXPORTS = ROOT / "review -2" / "dashboard_exports"
DOCS = ROOT / "docs"
DATA = DOCS / "data"


def load_server():
    spec = importlib.util.spec_from_file_location("cycloscope_server", DASHBOARD / "server.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def main() -> None:
    server = load_server()
    if not DOCS.resolve().is_relative_to(ROOT.resolve()) or DOCS.name != "docs":
        raise RuntimeError(f"Refusing to replace unsafe output path: {DOCS}")
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DATA.mkdir(parents=True)
    for name in ("index.html", "styles.css", "app.js"):
        shutil.copy2(STATIC / name, DOCS / name)
    index = (DOCS / "index.html").read_text(encoding="utf-8")
    index = index.replace("<meta name=\"viewport\"", "<meta name=\"deployment-mode\" content=\"static\">\n  <meta name=\"viewport\"")
    (DOCS / "index.html").write_text(index, encoding="utf-8")
    payloads = {
        "daily": server.DAILY,
        "hourly": server.HOURLY,
        "questions": server.QUESTIONS,
        "hypotheses": server.HYPOTHESES,
        "models": {"metrics": server.model_metrics(), "predictions": server.PREDICTIONS},
    }
    for name, payload in payloads.items():
        (DATA / f"{name}.json").write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    shutil.copy2(EXPORTS / "bike_sharing_daily_processed.csv", DATA / "daily.csv")
    shutil.copy2(EXPORTS / "bike_sharing_hourly_processed.csv", DATA / "hourly.csv")
    shutil.copy2(EXPORTS / "model_predictions.csv", DATA / "predictions.csv")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    print(f"GitHub Pages build created at {DOCS}")


if __name__ == "__main__":
    main()
