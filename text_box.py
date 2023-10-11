from playwright.sync_api import Page


def test_text_box(page: Page, data):
    page.goto(data['text_box']['url'])
    for value in data['text_box']['values']:
        page.locator('input#userName').fill(value['full_name'])
        page.locator('input#userEmail').fill(value['email'])
        page.locator('textarea#currentAddress').fill(value['current_address'])
        page.locator('textarea#permanentAddress').fill(value['perm_adrress'])

        page.locator('button#submit').click()

        assert page.locator('p#name').text_content().removeprefix('Name:') == value['full_name']
        assert page.locator('p#email').text_content().removeprefix('Email:') == value['email']
        assert page.locator('p#currentAddress').text_content().removeprefix('Current Address :').strip() == value[
            'current_address']
        assert page.locator('p#permanentAddress').text_content().removeprefix('Permananet Address :').strip() == value[
            'perm_adrress']
