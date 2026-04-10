from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def get_cart_items(self):
        names = self.driver.find_elements(*self.ITEM_NAME)
        prices = self.driver.find_elements(*self.ITEM_PRICE)

        return [(n.text, p.text) for n, p in zip(names, prices)]

    def get_cart_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))