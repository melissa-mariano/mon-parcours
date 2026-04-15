from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto("file:///C:/Users/mel96/Documents/mon parcours/cv.html")

    page.pdf(
        path="cv.pdf",
        format="A4",
        margin={"top": "1cm", "bottom": "1cm", "left": "1cm", "right": "1cm"},
        print_background=True
    )

    browser.close()