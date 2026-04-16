from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    PRODUCTS = (By.CLASS_NAME, "inventory_item")

    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCTS))
    
    def sort_products(self, option_text):
        from selenium.webdriver.support.ui import Select
        select = Select(self.find(self.SORT_CONTAINER))
        select.select_by_visible_text(option_text)

    def get_all_prices(self):
        prices = self.driver.find_elements(*self.INVENTORY_ITEM_PRICE)
        return [float(p.text.replace('$', '')) for p in prices]

    def add_item_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def remove_item(self):
        self.click(self.REMOVE_BTN)

    def is_remove_visible(self):
        return self.find(self.REMOVE_BTN).is_displayed()

    # 👉 FIX 3 (handle missing badge safely)
    def get_cart_count(self):
        elements = self.driver.find_elements(*self.CART_BADGE)
        return elements[0].text if elements else "0"

    def go_to_cart(self):
        self.click(self.CART_ICON)