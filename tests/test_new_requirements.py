import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture
def logged_in_driver(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert login.is_products_page()
    return driver

@pytest.mark.regression
def test_fr17_successful_logout(logged_in_driver):
    """
    FR-17: Successful Logout
    Given the user is logged into the application, 
    when the "Logout" link in the sidebar is clicked, 
    then the user is redirected to the Login page and the session is invalidated.
    """
    logger.info("Running FR-17: Successful Logout")
    product_page = ProductPage(logged_in_driver)
    product_page.logout()
    
    # After logout, we should be back at the login page
    login_page = LoginPage(logged_in_driver)
    # The login button should be visible again
    assert logged_in_driver.current_url == "https://www.saucedemo.com/" or "index.html" in logged_in_driver.current_url
    assert login_page.find(login_page.LOGIN_BTN).is_displayed()

@pytest.mark.regression
def test_fr18_product_sorting_price_low_to_high(logged_in_driver):
    """
    FR-18: Product Sorting (Price: Low to High)
    Given the user is on the Products page, 
    when the "Price (low to high)" sort option is selected, 
    then all items must be displayed in ascending order based on their price values.
    """
    logger.info("Running FR-18: Product Sorting (Price: Low to High)")
    product_page = ProductPage(logged_in_driver)
    
    # Select Price (low to high)
    product_page.sort_products("Price (low to high)")
    
    # Verify sorting
    prices = product_page.get_all_prices()
    logger.info(f"Retrieved prices: {prices}")
    
    # Check if ascending
    assert prices == sorted(prices), f"Prices are not sorted ascending: {prices}"
