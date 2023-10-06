import pytest
from playwright.sync_api import Page

from test_web_tables import test_web_tables
from text_box import test_text_box
from test_radio_button import test_radio_button
import json


class TestController():
    # data = json.load(open('data.json'))

    @pytest.fixture()
    def data(self):
        return json.load(open('data.json'))

    def test_text_box(self, page: Page, request):
        test_text_box(page, request.getfixturevalue('data')['text_box'])

    def test_radio_button(self, page: Page, request):
        test_radio_button(page, request.getfixturevalue('data')['radio_button'])

    def test_web_tables(self, page: Page, request):
        test_web_tables(page, request.getfixturevalue('data')['radio_button'])
