from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class DropdownPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dropdown"

    DROPDOWN = (By.ID, "dropdown")

    def open(self):
        self.driver.get(self.URL)

    def select_option(self, value):
        dropdown = Select(self.find(self.DROPDOWN))
        dropdown.select_by_value(value)

    def get_selected_option(self):
        dropdown = Select(self.find(self.DROPDOWN))
        return dropdown.first_selected_option.text
