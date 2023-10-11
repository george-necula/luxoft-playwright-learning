import pytest
from playwright.sync_api import Page
import requests
import json


@pytest.fixture()
def data():
    return json.load(open('data.json'))


@pytest.mark.skip
def test_nimic(page: Page, assert_snapshot, context):
    page.goto('https://demoqa.com/dynamic-properties')

    print()
