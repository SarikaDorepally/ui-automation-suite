import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pages.login_page import LoginPage
from pages.checkboxes_page import CheckboxesPage
from pages.dropdown_page import DropdownPage


class TestLogin:
    """TC01 & TC02 — Login Page (WebDriver + Locators + Explicit Waits)"""

    def test_valid_login(self, driver):
        """TC01: Valid credentials should navigate to secure area."""
        page = LoginPage(driver)
        page.open()
        page.login("tomsmith", "SuperSecretPassword!")
        assert "secure" in driver.current_url, "Expected redirect to /secure after login"
        assert "You logged into a secure area!" in page.get_flash_message()

    def test_invalid_login(self, driver):
        """TC02: Invalid credentials should show error flash message."""
        page = LoginPage(driver)
        page.open()
        page.login("wronguser", "wrongpass")
        flash = page.get_flash_message()
        assert "Your username is invalid!" in flash, f"Unexpected flash: {flash}"


class TestCheckboxes:
    """TC03 & TC04 — Checkboxes (Web Elements interaction)"""

    def test_check_all_checkboxes(self, driver):
        """TC03: All checkboxes should be checked after check_all()."""
        page = CheckboxesPage(driver)
        page.open()
        page.check_all()
        checkboxes = page.get_checkboxes()
        assert all(cb.is_selected() for cb in checkboxes), \
            "Not all checkboxes were checked"

    def test_uncheck_all_checkboxes(self, driver):
        """TC04: All checkboxes should be unchecked after uncheck_all()."""
        page = CheckboxesPage(driver)
        page.open()
        page.check_all()   # ensure all checked first
        page.uncheck_all()
        checkboxes = page.get_checkboxes()
        assert all(not cb.is_selected() for cb in checkboxes), \
            "Not all checkboxes were unchecked"


class TestDropdown:
    """TC05 — Dropdown (Select Web Element)"""

    def test_select_option_1(self, driver):
        """TC05: Selecting Option 1 from dropdown should reflect correctly."""
        page = DropdownPage(driver)
        page.open()
        page.select_option("1")
        selected = page.get_selected_option()
        assert selected == "Option 1", f"Expected 'Option 1', got '{selected}'"
