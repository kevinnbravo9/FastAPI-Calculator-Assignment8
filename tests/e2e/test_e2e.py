from playwright.sync_api import sync_playwright


def test_calculator_addition():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        page = browser.new_page()
        page.goto("http://localhost:8000")

        page.fill("#a", "2")
        page.fill("#b", "3")
        page.click("button#add")

        result = page.inner_text("#result")

        assert result == "Result: 5"

        browser.close()