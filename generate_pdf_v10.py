from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Atualize com o caminho correto do seu computador se necessário
    page.goto("file:///C:/Users/mel96/Documents/mon parcours/cv_v10.html")
    
    # Aguarda o carregamento completo para evitar fontes quebradas
    page.evaluate("document.fonts.ready")

    page.pdf(
        path="cv_v10.pdf",
        format="A4",
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        print_background=True,
        scale=1.0,
        page_ranges="1"  # Força 1 página perfeitamente
    )

    browser.close()