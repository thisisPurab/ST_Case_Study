import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime


# ---------------- DRIVER FIXTURE ---------------- #
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


# ---------------- HOOK: SCREENSHOT + REPORT ---------------- #
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        extra = getattr(report, "extra", [])

        if report.failed:
            driver = item.funcargs.get("driver", None)
            if driver:
                os.makedirs("reports/screenshots", exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f"{item.name}_{timestamp}.png"
                file_path = os.path.join("reports/screenshots", file_name)

                driver.save_screenshot(file_path)

                # attach screenshot to HTML report
                try:
                    import pytest_html
                    extra.append(pytest_html.extras.image("../screenshots/" + file_name))
                except Exception:
                    pass

        report.extra = extra