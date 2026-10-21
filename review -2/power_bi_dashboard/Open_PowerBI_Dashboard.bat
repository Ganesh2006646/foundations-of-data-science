@echo off
echo ============================================================
echo   Opening Capital Bikeshare Power BI Project (.pbip)
echo   Foundations of Data Science - Lab Evaluation 2
echo ============================================================
echo.

set PBIP_FILE="%~dp0Bike_Sharing_Dashboard.pbip"
set PBI_EXE="C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe"

if exist %PBI_EXE% (
    echo Launching Power BI Desktop...
    start "" %PBI_EXE% %PBIP_FILE%
) else (
    echo Power BI Desktop executable not found in default path.
    echo Opening file with default Windows handler...
    start "" %PBIP_FILE%
)

echo Done. Check your taskbar for Power BI Desktop!
