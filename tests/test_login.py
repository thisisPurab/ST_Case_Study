import pytest
import json
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)

with open("testdata/login_data.json") as f:
    test_data = json.load(f)


@pytest.mark.regression
@pytest.mark.parametrize("data", test_data)
def test_login_data_driven(driver, data):
    logger.info(f"Running test: {data}")

    login = LoginPage(driver)
    login.load()
    login.login(data["username"], data["password"])

    if data["expected"] == "success":
        assert login.is_products_page()
    else:
        assert "Epic sadface" in login.get_error()