from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckboxesPage(BasePage):
    URL = "https://the-internet.herokuapp.com/checkboxes"

    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def open(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)

    def check_all(self):
        for box in self.get_checkboxes():
            if not box.is_selected():
                box.click()

    def uncheck_all(self):
        for box in self.get_checkboxes():
            if box.is_selected():
                box.click()
