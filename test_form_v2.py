from playwright.sync_api import Locator


# cate o functie pentru fiecare tip de field gasit

def fill_in_input_field(value: str | list, row: Locator) -> None:
    if row.locator('input').count() == 2:
        row.locator('input').all()[0].fill(value[0])
        row.locator('input').all()[1].fill(value[1])
    elif row.locator('input').count() == 1:
        row.locator('input').fill(value)


def get_property_row_by_label(label: str) -> Locator:
    ...


def identify_form_field_from_row(row: Locator):  # return function

    if row.locator('input[type=text]').count():
        return fill_in_input_field


def fill_in_form(propertys_dict: dict) -> None:
    ...

# propertys_dict: {"label din ui": value}
