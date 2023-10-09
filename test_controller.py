import pytest
from playwright.sync_api import Page
import requests

from test_broken_links_images import broken_links_images
from test_buttons import buttons
from test_links import links
from test_web_tables import web_tables
from text_box import text_box
from test_radio_button import radio_button
import json


class TestController:
    # data = json.load(open('data.json'))

    @pytest.fixture()
    def data(self):
        return json.load(open('data.json'))

    def test_text_box(self, page: Page, request):
        text_box(page, request.getfixturevalue('data')['text_box'])

    def test_radio_button(self, page: Page, request):
        radio_button(page, request.getfixturevalue('data')['radio_button'])

    def test_web_tables(self, page: Page, request):
        web_tables(page, request.getfixturevalue('data')['web_tables'])

    def test_buttons(self, page: Page):
        buttons(page)

    def test_broken_links_images(self, page: Page):
        broken_links_images(page)

    @pytest.mark.xfail
    def test_links(self, page: Page, assert_snapshot, context):
        links(page, assert_snapshot, context)

    def test_nimic(self, page: Page, assert_snapshot, context):
        page.goto('https://demoqa.com/broken')
        print(requests.get(url='https://demoqa.com/images/Toolsqa.jpg', verify=False))

        print()
