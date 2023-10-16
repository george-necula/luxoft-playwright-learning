from playwright.sync_api import Page


def test_modals(page: Page):
    page.goto('https://demoqa.com/modal-dialogs')

    for button in page.locator('div#modalWrapper > div > button').all():
        # get button text
        text = button.text_content().lower()
        # open modal
        button.click()
        title = page.locator('div.modal-header').text_content().lower()
        # compare title with button title
        assert title.startswith(text)

        page.locator('div.modal-footer > button').click()
    print()
