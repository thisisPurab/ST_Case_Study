import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.regression
def test_checkout_blank_first_name(driver):
    logger.info("Starting test_checkout_blank_first_name")

    # Step 1: Login
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Step 2: Add item to cart (precondition)
    product = ProductPage(driver)
    product.add_item_to_cart()

    # Step 3: Go to checkout
    checkout = CheckoutPage(driver)
    checkout.go_to_checkout()

    # Step 4: Leave first name blank
    checkout.fill_details("", "Shah", "400001")
    checkout.click_continue()

    # Step 5: Verify error
    assert "Error" in checkout.get_error()

    logger.info("Checkout validation passed for blank first name")