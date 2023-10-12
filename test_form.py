from playwright.sync_api import Page
import re


def collect_data(page: Page):
    return_data = dict()

    for row in page.locator('table > tbody > tr').all():

        key, value = row.locator('td:nth-child(1)').text_content(), row.locator('td:nth-child(2)').text_content()
        if not value:
            continue
        if key == 'Student Name':
            return_data['first name'], return_data['last name'] = value.split(' ')
        elif key == 'Subjects':
            return_data['subjects'] = [subject.strip().lower() for subject in value.split(',')]
        elif key == 'Hobbies':
            return_data['hobbies'] = [hobby.lower() for hobby in value.split(' ')]
        elif key == 'State and City':
            return_data['state'], return_data['city'] = value.split(' ')
        else:
            return_data[key.lower()] = value
    return return_data


def fill_fields(page, form_values):
    for key, value in form_values.items():
        match key:
            case 'first name':
                page.get_by_placeholder('First name').fill(value)
            case 'last name':
                page.get_by_placeholder('Last name').fill(value)
            case 'student email':
                page.get_by_placeholder('name@example.com').fill(value)
            case 'gender':
                page.locator(f'label:text-is("{value}")').first.check()
            case 'mobile':
                page.get_by_placeholder('Mobile Number').fill(value)
            case 'date of birth':
                page.locator('input#dateOfBirthInput').fill(value)
            case 'hobbies':
                for hobby in value:
                    page.get_by_text(re.compile(f'^{hobby}$', re.IGNORECASE)).click()
            case 'picture':
                with page.expect_file_chooser() as fc_info:
                    page.locator('input#uploadPicture').click()
                file_chooser = fc_info.value
                file_chooser.set_files(value)
            case 'subjects':
                for subject in value:
                    page.locator('div.subjects-auto-complete__input > input').fill(subject)
                    page.keyboard.press('Enter', delay=10)
            case 'address':
                page.get_by_placeholder('Current Address').fill(value)
            case 'state':
                page.locator('div:text-is("Select State")').first.click()  # deschide lista pentru 'state'
                page.locator(f'div:text-is("{value}")').first.click()
            case 'city':
                page.locator('div:text-is("Select City")').first.click()  # deschide lista pentru 'city'
                page.locator(f'div:text-is("{value}")').first.click()


def test_forms(page: Page, assert_snapshot, data):
    page.goto('https://demoqa.com/automation-practice-form')

    for current_data in data['form']['values']:
        fill_fields(page, current_data)
        page.evaluate('document.getElementById("submit").click()')

        assert collect_data(page) == current_data

        page.evaluate('document.getElementById("closeLargeModal").click()')
    print()
