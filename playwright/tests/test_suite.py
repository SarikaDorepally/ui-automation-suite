import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://the-internet.herokuapp.com"


# ── TC01: Valid Login ────────────────────────────────────────────────────────
def test_valid_login(page: Page):
    """
    Playwright: Browser → Context → Page hierarchy.
    Auto-waiting: no explicit waits needed — Playwright waits for elements automatically.
    """
    page.goto(f"{BASE_URL}/login")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(f"{BASE_URL}/secure")
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")


# ── TC02: Invalid Login ──────────────────────────────────────────────────────
def test_invalid_login(page: Page):
    """Playwright: get_by_text locator + auto-wait on flash message."""
    page.goto(f"{BASE_URL}/login")

    page.locator("#username").fill("baduser")
    page.locator("#password").fill("badpass")
    page.get_by_role("button", name="Login").click()

    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")


# ── TC03: Check All Checkboxes ───────────────────────────────────────────────
def test_check_all_checkboxes(page: Page):
    """Playwright: Actions — clicking multiple elements."""
    page.goto(f"{BASE_URL}/checkboxes")

    checkboxes = page.locator("input[type='checkbox']")
    count = checkboxes.count()

    for i in range(count):
        cb = checkboxes.nth(i)
        if not cb.is_checked():
            cb.check()

    for i in range(count):
        expect(checkboxes.nth(i)).to_be_checked()


# ── TC04: Dropdown Selection ─────────────────────────────────────────────────
def test_dropdown_select(page: Page):
    """Playwright: select_option action on a dropdown element."""
    page.goto(f"{BASE_URL}/dropdown")

    page.locator("#dropdown").select_option(value="1")
    expect(page.locator("#dropdown")).to_have_value("1")


# ── TC05: Page Title Verification ────────────────────────────────────────────
def test_homepage_title(page: Page):
    """Playwright: Basic navigation + title assertion."""
    page.goto(BASE_URL)

    expect(page).to_have_title("The Internet")
    expect(page.get_by_role("heading", name="Welcome to the-internet")).to_be_visible()
