from playwright.sync_api import Page


def test_tabs(page: Page):
    page.goto('https://demoqa.com/tabs')

    for tab in page.locator('nav[role=tablist] > a').all():
        # try catch is a must in this case because there isn't
        # a way to check whether a locator has an attribute, only it's value
        try:
            if not tab.get_attribute('aria-disabled'):
                tab.click()
        except:
            ...

    print()
