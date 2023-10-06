from playwright.sync_api import Page


def test_web_tables(page: Page, data):
    page.goto(data['url'])
