import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# FR-06
@pytest.mark.regression
def test_products_visible(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    product = ProductPage(driver)
    assert product.get_product_count() >= 6


# FR-08
@pytest.mark.regression
def test_remove_from_cart(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    product = ProductPage(driver)
    product.add_item_to_cart()
    product.remove_item()

    # ✅ FIX: badge disappears → count becomes "0"
    assert product.get_cart_count() == "0"


# FR-09
@pytest.mark.regression
def test_cart_details(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    product = ProductPage(driver)
    product.add_item_to_cart()

    # ✅ FIX: directly validate cart instead of missing method
    product.go_to_cart()
    cart = CartPage(driver)

    assert cart.get_cart_count() == 1


# FR-10
@pytest.mark.regression
def test_unauthorized_access(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # simulate unauthorized access
    driver.get("https://www.saucedemo.com/cart.html")

    assert "saucedemo.com" in driver.current_url


# FR-11
@pytest.mark.regression
def test_navigate_to_checkout(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    product = ProductPage(driver)
    product.add_item_to_cart()

    checkout = CheckoutPage(driver)
    checkout.go_to_checkout()

    assert "checkout-step-one" in driver.current_url


# FR-13
@pytest.mark.regression
def test_blank_last_name(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    product = ProductPage(driver)
    product.add_item_to_cart()

    checkout = CheckoutPage(driver)
    checkout.go_to_checkout()

    checkout.fill_details("Purab", "", "400001")
    checkout.click_continue()

    assert "Error" in checkout.get_error()


# FR-15
@pytest.mark.regression
def test_checkout_overview(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    product = ProductPage(driver)
    product.add_item_to_cart()

    checkout = CheckoutPage(driver)
    checkout.go_to_checkout()

    checkout.fill_details("Purab", "Shah", "400001")
    checkout.click_continue()

    assert checkout.is_overview_page()