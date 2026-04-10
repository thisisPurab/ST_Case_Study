import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.smoke
def test_finish_order(driver):
    logger.info("Starting test_finish_order")

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

    # Step 4: Fill valid details
    checkout.fill_details("Purab", "Shah", "400001")
    checkout.click_continue()

    # Step 5: Finish order
    checkout.click_finish()

    # Step 6: Verify success
    assert "Thank you for your order" in checkout.get_success_message()

    logger.info("Order completed successfully")