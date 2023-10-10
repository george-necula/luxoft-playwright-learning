from playwright.sync_api import Page


def forms(page: Page, assert_snapshot):
    page.goto('https://demoqa.com/automation-practice-form')

    page.get_by_placeholder('First name').fill('altceva')
    page.get_by_placeholder('Last name').fill('altceva')
    page.get_by_placeholder('name@example.com').fill('cevamail@ceva.com')
    page.locator('label:text-is("Male")').first.check()
    page.get_by_placeholder('Mobile Number').fill('6465465464')
    page.locator('input#dateOfBirthInput').fill('10 Oct 2020')
    page.keyboard.press('Escape', delay=100)
    page.keyboard.press('Escape', delay=100)
    page.locator('div.subjects-auto-complete__input > input').fill('ceva subiect')
    page.locator('label:text-is("Reading")').first.check()

    with page.expect_file_chooser() as fc_info:
        page.locator('input#uploadPicture').click()
    file_chooser = fc_info.value
    file_chooser.set_files("screenshot_original.jpg")

    page.get_by_placeholder('Current Address').fill('ceva adresa')

    page.locator('div:text-is("Select State")').first.click()  # deschide lista pentru 'state'
    page.locator('div:text-is("NCR")').first.click()

    page.locator('div:text-is("Select City")').first.click()  # deschide lista pentru 'city'
    page.locator('div:text-is("Delhi")').first.click()

    page.evaluate('document.getElementById("submit").click()')

    assert_snapshot(page.locator('div.table-responsive').screenshot(), 'screenshot_form_table.jpg')

    print()
