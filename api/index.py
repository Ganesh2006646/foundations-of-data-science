"""Vercel Python Function entry point for the CycleScope analytics API."""

from pathlib import Path
import sys


dashboard_dir = Path(__file__).resolve().parents[1] / "review -2" / "dashboard"
sys.path.insert(0, str(dashboard_dir))

from server import Handler as handler  # noqa: E402,F401
