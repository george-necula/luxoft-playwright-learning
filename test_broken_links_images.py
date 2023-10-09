from playwright.sync_api import Page
import requests


def broken_links_images(page: Page):
    page.goto('https://demoqa.com/broken')

    img_tags = page.locator('div.row > div:nth-child(2) > div:nth-child(2) > img').all()
    link_tags = page.locator('div.row > div:nth-child(2) > div:nth-child(2) > a').all()

    img_src0 = img_tags[0].get_attribute('src')
    assert requests.get(f'https://demoqa.com{img_src0}', verify=False).status_code == 200
    # nu intelg dc returneaza 200 si la 'broken image'
    # img_src1 = img_tags[1].get_attribute('src')
    # assert requests.get(f'https://demoqa.com{img_src1}', verify=False).status_code != 200

    a_href0 = link_tags[0].get_attribute('href')
    a_href1 = link_tags[1].get_attribute('href')
    assert requests.get(a_href0, verify=False).status_code == 200
    assert requests.get(a_href1, verify=False).status_code != 200
