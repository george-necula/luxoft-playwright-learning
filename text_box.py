from playwright.sync_api import Page


# data = dict(text_box1=dict(url='https://demoqa.com/text-box',
#                            full_name='Full Name',
#                            email='name@example.com',
#                            current_address='210-8377 Interdum. St.',
#                            perm_adrress='Ap #227-5804 Nibh Ave'),
#             text_box2=dict(url='https://demoqa.com/text-box',
#                            full_name='Full Name 2',
#                            email='name2@example.com',
#                            current_address='210-8377 Interdum. St. part 2',
#                            perm_adrress='Ap #227-5804 Nibh Ave part2'),
#             )


def test_text_box(page: Page, data):
    page.goto(data['url'])
    for value in data['values']:
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
        # print(value['full_name'])
