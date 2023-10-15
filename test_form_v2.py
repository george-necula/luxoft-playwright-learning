from playwright.sync_api import Locator, Page
import re


# cate o functie pentru fiecare tip de field gasit

def fill_in_input_field(page, values: str | list, row: Locator) -> None:
    if row.locator('input').count() == 2:
        row.locator('input').all()[0].fill(values[0])
        row.locator('input').all()[1].fill(values[1])
    elif row.locator('input').count() == 1:
        row.locator('input').fill(values)


def fill_in_radio_or_check_field(page, values: str | list, row: Locator) -> None:
    if type(values) == str:
        row.locator(f'label:text-matches("^{values}$","i")').first.check()
    else:
        for value in values:
            row.locator(f'label:text-matches("^{value}$","i")').first.check()


def fill_in_subjects_field(page, values: list, row: Locator) -> None:
    for subject in values:
        row.locator('input').fill(subject)
        page.keyboard.press('Enter', delay=10)


def fill_in_file_field(page, value: str, row: Locator) -> None:
    with page.expect_file_chooser() as fc_info:
        row.locator('input#uploadPicture').click()
    file_chooser = fc_info.value
    file_chooser.set_files(value)


def fill_in_textarea_field(page, value: str, row: Locator) -> None:
    row.locator('textarea').fill(value)


def fill_in_subjects_or_state_field(page, values: list, row: Locator) -> None:
    if row.locator('input').count() == 1:
        for subject in values:
            row.locator('input').fill(subject)
            page.keyboard.press('Enter', delay=10)
    else:
        row.locator('div:has(input)').all()[0].click()
        row.locator(f'div:text-matches("^{values[0]}$","i")').first.click()

        row.locator('div:has(input)').all()[1].click()
        row.locator(f'div:text-matches("^{values[1]}$","i")').first.click()


def get_property_row_by_label(page: Page, label: str) -> Locator:
    if label == 'gender':
        return page.locator('form > div.row:has(div:has-text("gender"))')
    else:
        return page.locator(f'form > div.row:has(label:has-text("{label}"))')


def identify_form_field_from_row(row: Locator):  # return function
    if row.locator('input[aria-autocomplete=list]').count():
        return fill_in_subjects_or_state_field
    if row.locator('input[type=text]').count():
        return fill_in_input_field
    elif row.locator('input[type=radio]').count() or row.locator('input[type=checkbox]').count():
        return fill_in_radio_or_check_field
    elif row.locator('input[type=file]').count():
        return fill_in_file_field
    elif row.locator('textarea').count():
        return fill_in_textarea_field


def fill_in_form(page, property_dict: dict) -> None:
    for key, value in property_dict.items():
        row = get_property_row_by_label(page, key)
        fill_func = identify_form_field_from_row(row)
        fill_func(page, value, row)


# propertys_dict: {"label din ui": value}

def test_test(page, data):
    page.goto('https://demoqa.com/automation-practice-form')

    fill_in_form(page, data['form']['values'][0])

    print()
