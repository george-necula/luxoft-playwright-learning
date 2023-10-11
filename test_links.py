from playwright.sync_api import Page


def test_links(page: Page, assert_snapshot, context):
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

    with page.expect_request("https://demoqa.com/created") as first:
        page.locator("a#created").click()
    assert first.value.response().status == 201

    with page.expect_request("https://demoqa.com/no-content") as first:
        page.locator("a#no-content").click()
    assert first.value.response().status == 204

    with page.expect_request("https://demoqa.com/moved") as first:
        page.locator("a#moved").click()
    assert first.value.response().status == 301

    with page.expect_request("https://demoqa.com/bad-request") as first:
        page.locator("a#bad-request").click()
    assert first.value.response().status == 400

    with page.expect_request("https://demoqa.com/unauthorized") as first:
        page.locator("a#unauthorized").click()
    assert first.value.response().status == 401

    with page.expect_request("https://demoqa.com/forbidden") as first:
        page.locator("a#forbidden").click()
    assert first.value.response().status == 403

    with page.expect_request("https://demoqa.com/invalid-url") as first:
        page.locator("a#invalid-url").click()
    assert first.value.response().status == 404
