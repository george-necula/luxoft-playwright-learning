from playwright.sync_api import Page


def test_buttons(page: Page):
    page.goto('https://demoqa.com/buttons')

    page.locator('button#doubleClickBtn').dblclick()
    page.locator('button#rightClickBtn').click(button="right")
    page.locator('button#rightClickBtn').focus()
    page.keyboard.press("Tab")
    page.keyboard.press("Space")

    assert page.locator('p#doubleClickMessage').inner_text() == 'You have done a double click'
    assert page.locator('p#rightClickMessage').inner_text() == 'You have done a right click'
    assert page.locator('p#dynamicClickMessage').inner_text() == 'You have done a dynamic click'
