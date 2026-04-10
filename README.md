# SauceDemo Automation & Performance Testing

## Overview

This project implements:

-   Selenium-based UI automation (PyTest + POM)
-   Data-driven testing
-   HTML reporting with screenshots
-   Performance testing using Apache JMeter

---

## Tech Stack

-   Python 3.x
-   PyTest
-   Selenium WebDriver
-   pytest-html
-   Apache JMeter

---

## Project Structure

```text
ST_Case_STudy/
│── pages/
│── performance/
│── reports/
│── testdata/
│── tests/
│── utils/
│── conftest.py
│── pytest.ini
│── README.md
│── requirements.txt
```

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd ST_Case_STudy
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Chrome

Ensure Google Chrome is installed on your system.

---

## Running Tests

### Run Smoke Tests

```bash
pytest -m smoke -v
```

---

### Run Full Test Suite

```bash
pytest -v
```

---

### Run with HTML Report

```bash
pytest --html=reports/html/report.html --self-contained-html -v
```

---

## Test Reports

-   HTML Report:

```bash
reports/html/report.html
```

-   Screenshots (on failure):

```bash
reports/screenshots/
```

---

## Performance Testing (JMeter)

### Run Test Plan

```bash
jmeter -n -t performance/jmx/sauce_demo.jmx -l performance/results/results.jtl
```

---

### Generate HTML Dashboard

```bash
jmeter -g performance/results/results.jtl -o html_report
```

---
