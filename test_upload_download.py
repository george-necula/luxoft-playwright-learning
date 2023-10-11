from playwright.sync_api import Page


def test_upload_download(page: Page):
    page.goto('https://demoqa.com/upload-download')

    with page.expect_download() as download_info:
        page.locator('a#downloadButton').click()
    download = download_info.value
    assert download.suggested_filename == 'sampleFile.jpeg'

    with page.expect_file_chooser() as fc_info:
        page.locator('input#uploadFile').click()
    file_chooser = fc_info.value
    file_chooser.set_files("screenshot_original.jpg")

    assert page.locator('p#uploadedFilePath').text_content().endswith('screenshot_original.jpg')
