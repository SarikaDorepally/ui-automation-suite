# UI Automation Suite — Selenium & Playwright

A cross-framework end-to-end test automation suite covering 10 test scenarios using **Selenium (Python + POM)** and **Playwright (Python + pytest-playwright)** on [the-internet.herokuapp.com](https://the-internet.herokuapp.com).

---

## Framework Comparison

| Feature | Selenium | Playwright |
|---|---|---|
| Waits | Explicit (`WebDriverWait`) + Implicit | Auto-waiting built-in |
| Locators | By.ID, By.CSS, By.XPATH | `locator()`, `get_by_role()`, `get_by_text()` |
| Architecture | WebDriver → Browser | Browser → Context → Page |
| Test Runner | pytest | pytest-playwright |
| POM Support | Manual class structure | Manual class structure |
| Speed | Moderate | Faster (async-native) |

---

## Project Structure

```
automation_suite/
├── selenium/
│   ├── pages/
│   │   ├── base_page.py        # BasePage with explicit wait helpers
│   │   ├── login_page.py       # Login page POM
│   │   ├── checkboxes_page.py  # Checkboxes page POM
│   │   └── dropdown_page.py    # Dropdown page POM
│   ├── tests/
│   │   └── test_suite.py       # 5 Selenium test cases
│   └── conftest.py             # Chrome WebDriver fixture
├── playwright/
│   ├── tests/
│   │   └── test_suite.py       # 5 Playwright test cases
│   └── conftest.py
├── requirements.txt
└── README.md
```

---

## Test Cases Covered

### Selenium (5 tests)
| ID | Test | Concepts Used |
|---|---|---|
| TC01 | Valid login → redirect to /secure | WebDriver, Locators, Explicit Wait |
| TC02 | Invalid login → flash error message | CSS Selector, Expected Conditions |
| TC03 | Check all checkboxes | Web Elements, find_elements |
| TC04 | Uncheck all checkboxes | Web Elements, is_selected() |
| TC05 | Dropdown Option 1 selection | Select class, select_by_value |

### Playwright (5 tests)
| ID | Test | Concepts Used |
|---|---|---|
| TC01 | Valid login → redirect | page.goto, fill, get_by_role, expect |
| TC02 | Invalid login → error | locator, to_contain_text |
| TC03 | Check all checkboxes | locator.nth(), is_checked(), check() |
| TC04 | Dropdown select | select_option, to_have_value |
| TC05 | Homepage title check | to_have_title, get_by_role |

---

## Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Run Selenium tests
cd selenium
pytest tests/ -v

# Run Playwright tests
cd playwright
pytest tests/ -v
```

---

## Key Concepts Demonstrated

**Selenium:**
- `WebDriver` setup with ChromeOptions (headless mode)
- Locators: ID, CSS Selector, XPath
- `WebDriverWait` + `expected_conditions` for explicit waits
- Page Object Model (POM) with `BasePage` inheritance
- `Select` class for dropdown interactions

**Playwright:**
- Browser → Context → Page hierarchy
- Auto-waiting (no explicit waits needed)
- Locators: `locator()`, `get_by_role()`, `get_by_text()`
- Actions: `fill()`, `click()`, `check()`, `select_option()`
- Assertions with `expect()` API
- `pytest-playwright` test runner integration
