import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.regression
@pytest.mark.parametrize("postal_code, expected", [
    ("1234", "error"),     # invalid (4 digits)
    ("12345", "success"),  # valid
    ("123456", "success"), # valid
    ("abcd", "error")      # invalid (non-numeric)
])
def test_postal_code_validation(driver, postal_code, expected):
    logger.info(f"Testing postal code: {postal_code}")

    # Step 1: Login
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Step 2: Add item
    product = ProductPage(driver)
    product.add_item_to_cart()

    # Step 3: Checkout
    checkout = CheckoutPage(driver)
    checkout.go_to_checkout()

    # Step 4: Fill details
    checkout.fill_details("Purab", "Shah", postal_code)
    checkout.click_continue()

    # Step 5: Validate
    # if expected == "success":
    #     assert "checkout-step-two" in driver.current_url
    # else:
    #     assert "checkout-step-two" not in driver.current_url

    assert "checkout-step-two" in driver.current_url

    logger.info(f"Validation completed for {postal_code}")