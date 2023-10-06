from playwright.sync_api import Page


def test_radio_button(page: Page, data):
    page.goto(data['url'])

    for value in data['values']:
        page.locator('div[class=\"custom-control custom-radio custom-control-inline\"]').filter(
            has_text=value['answer']).click()

        assert page.locator('span.text-success').text_content() == value['answer']
        # print(value['answer'])