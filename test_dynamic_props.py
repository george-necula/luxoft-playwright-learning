from playwright.sync_api import Page


def dynamic_props(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')

    first_p = page.locator('div.row > div:nth-child(2) > div:nth-child(2) > p').first
    assert first_p.text_content() == 'This text has random Id'

    page.click('div.row > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)')
    buttons = page.locator('div.row > div:nth-child(2) > div:nth-child(2) > button').all()

    assert buttons[0].text_content() == 'Will enable 5 seconds'
    assert 'text-danger' in buttons[1].get_attribute('class')
    assert buttons[2].text_content() == 'Visible After 5 Seconds'
    print()
