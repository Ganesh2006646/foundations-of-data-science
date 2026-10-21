$ErrorActionPreference = "Stop"
$dashboardRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
python (Join-Path $dashboardRoot "server.py")
