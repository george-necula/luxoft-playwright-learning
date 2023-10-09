from playwright.sync_api import Page


def links(page: Page, assert_snapshot, context):
    page.goto('https://demoqa.com/links')

    with context.expect_page() as new_page_info:
        page.locator('a#simpleLink').click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    assert_snapshot(new_page.screenshot(full_page=True), 'screenshot_original.png')
    new_page.close()

    page.locator('a#simpleLink').focus()
    page.keyboard.press("Tab")
    with context.expect_page() as new_page_info:
        page.locator('a#dynamicLink').click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()
    assert_snapshot(new_page.screenshot(full_page=True), 'screenshot_original.png')
    new_page.close()
