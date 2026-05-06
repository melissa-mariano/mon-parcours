from playwright.sync_api import sync_playwright
import time
import os

# Ajuste este caminho para o local do seu arquivo HTML
HTML_PATH = os.path.abspath("cv_bu_fixed.html")
OUTPUT_PDF = "cv_bu.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Carrega o HTML
    page.goto(f"file:///{C:\Users\mel96\Documents\mon parcours\cv_bu.html}")

    # Aguarda fontes e recursos carregarem completamente
    page.wait_for_load_state("networkidle")
    page.evaluate("() => document.fonts.ready")
    time.sleep(1)  # margem extra para fontes Google

    # Gera o PDF
    page.pdf(
        path=OUTPUT_PDF,
        format="A4",
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        print_background=True,
        scale=1.0,
        # REMOVIDO: page_ranges="1" — estava cortando o conteúdo
    )

    browser.close()
    print(f"✅ PDF gerado: {OUTPUT_PDF}")
