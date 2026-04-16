@echo off
cd /d %~dp0

@REM echo ==============================
@REM echo Running Pytest (Selenium Tests)
@REM echo ==============================
@REM python -m pytest --html=reports/html/report.html --self-contained-html -v

@REM echo.
@REM echo ==============================
@REM echo Opening Pytest Report
@REM echo ==============================
@REM start "" "reports/html/report.html"

echo.
echo ==============================
echo Running JMeter Test Plan
echo ==============================
jmeter -n -t performance/jmx/sauce_demo.jmx -l performance/results/results.jtl

echo.
echo ==============================
echo Generating JMeter HTML Report
echo ==============================
jmeter -g performance/results/results.jtl -o performace/html_report

echo.
echo ==============================
echo Opening JMeter Report
echo ==============================
start "" "performace/html_report/index.html"

echo.
echo All tasks completed!
pause