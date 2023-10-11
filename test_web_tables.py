from playwright.sync_api import Page


def test_web_tables(page: Page, data):
    page.goto(data['web_tables']['url'])

    for value in data['web_tables']['values']:
        page.locator('button#addNewRecordButton').click()
        page.locator('input#firstName').fill(value['firstName'])
        page.locator('input#lastName').fill(value['lastName'])
        page.locator('input#userEmail').fill(value['email'])
        page.locator('input#age').fill(value['age'])
        page.locator('input#salary').fill(value['salary'])
        page.locator('input#department').fill(value['department'])

        page.locator('button#submit').click()

        # assert page.locator('input#firstName') == value['firstName']
        # assert page.locator('input#lastName') == value['lastName']
        # assert page.locator('input#userEmail') == value['email']
        # assert page.locator('input#age') == value['age']
        # assert page.locator('input#salary') == value['salary']
        # assert page.locator('input#department') == value['department']
