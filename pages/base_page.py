# # pages/base_page.py

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class BasePage:
#     # Sidebar Locators
#     BURGER_MENU = (By.ID, "react-burger-menu-btn")
#     LOGOUT_LINK = (By.ID, "logout_sidebar_link")
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#         self.slow_mode_delay = 1  # Seconds to wait between actions

#     def find(self, locator):
#         return self.wait.until(EC.presence_of_element_located(locator))

#     def click(self, locator):
#         time.sleep(self.slow_mode_delay)
#         element = self.wait.until(EC.element_to_be_clickable(locator))
#         try:
#             element.click()
#         except Exception:
#             self.driver.execute_script("arguments[0].click();", element)

#     def type(self, locator, text):
#         time.sleep(self.slow_mode_delay)
#         element = self.find(locator)
#         element.clear()
#         element.send_keys(text)

#     def get_text(self, locator):
#         return self.find(locator).text

#     def open_menu(self):
#         self.click(self.BURGER_MENU)

#     def logout(self):
#         self.open_menu()
#         self.click(self.LOGOUT_LINK)

# pages/base_page.py

from selenium.webdriver.common.by import By

class BasePage:
    # Sidebar Locators
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    # ---------- BASIC ACTIONS ---------- #

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        element = self.find(locator)
        try:
            element.click()
        except Exception:
            # Fallback if normal click fails
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    # ---------- COMMON FLOWS ---------- #

    def open_menu(self):
        self.click(self.BURGER_MENU)

    def logout(self):
        self.open_menu()
        self.click(self.LOGOUT_LINK)