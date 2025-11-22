from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # launch a Chromium browser (headless=False lets you see it)
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    # create a new page
    page = browser.new_page()

    # go to the specific website
    page.goto("https://playwright.dev/python")

    # wait a bit so you can see the page
    #page.wait_for_timeout(5000)

    # close the browser
    browser.close()