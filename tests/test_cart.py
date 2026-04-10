import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.smoke
def test_add_to_cart(driver):
    logger.info("Starting test_add_to_cart")

    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    product = ProductPage(driver)
    product.add_item_to_cart()

    assert product.get_cart_count() == "1"
    assert product.is_remove_visible()

    logger.info("Add to cart test passed")