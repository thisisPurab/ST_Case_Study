import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime


# ---------------- DRIVER FIXTURE ---------------- #
@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless") 
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    options.add_argument("--disable-infobars")
    
    # Disable "Save password" prompts and credential manager
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "password_manager_leak_detection": False,
        "profile.default_content_setting_values.notifications": 2,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    
    # Disable automation-related popups and search engine choice
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=SafeBrowsingPasswordCheck")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
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