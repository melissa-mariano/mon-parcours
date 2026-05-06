from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto("file:///C:/Users/mel96/Documents/mon parcours/cv_accueil.html")
    
    page.evaluate("document.fonts.ready")

    page.pdf(
        path="cv_accueil.pdf",
        format="A4",
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        print_background=True,
        scale=1.0,
        page_ranges="1"
    )

    browser.close()