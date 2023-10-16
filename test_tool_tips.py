from playwright.sync_api import Page


def test_tool_tips(page: Page):
    page.goto('https://demoqa.com/tool-tips')
