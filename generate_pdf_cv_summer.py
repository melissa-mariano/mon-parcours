from playwright.sync_api import sync_playwright
import time

HTML_URL = "file:///C:/Users/mel96/Documents/mon parcours/cv_summer.html"
OUTPUT_PDF = r"C:\Users\mel96\Documents\mon parcours\cv_summer.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto(HTML_URL)
    page.wait_for_load_state("networkidle")
    page.evaluate("() => document.fonts.ready")
    time.sleep(1)

    page.pdf(
        path=OUTPUT_PDF,
        format="A4",
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        print_background=True,
        scale=1.0,
        page_ranges="1"
    )

    browser.close()
    print(f"✅ PDF gerado: {OUTPUT_PDF}")