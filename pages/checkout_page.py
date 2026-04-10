from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BTN = (By.ID, "checkout")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    OVERVIEW_CONTAINER = (By.ID, "checkout_summary_container")

    # 👉 ADD THESE (FIX 1)
    FINISH_BTN = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def go_to_checkout(self):
        self.click(self.CART_ICON)
        self.click(self.CHECKOUT_BTN)

    def fill_details(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)

    def is_overview_page(self):
        return self.find(self.OVERVIEW_CONTAINER).is_displayed()

    # 👉 ADD THESE (FIX 1)
    def click_finish(self):
        self.click(self.FINISH_BTN)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)