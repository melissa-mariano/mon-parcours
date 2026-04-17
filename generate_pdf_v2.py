from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto("file:///C:/Users/mel96/Documents/mon parcours/cv_v2.html")

    page.pdf(
        path="cv_v2.pdf",
        format="A4",
        margin={"top": "0.5cm", "bottom": "0.5cm", "left": "0.5cm", "right": "0.5cm"},
        print_background=True,
        scale=0.95  # Reduz o tamanho de tudo em 5%. Ajuste entre 0.85 e 0.99 até caber.
    )

    browser.close()