import asyncio
from playwright.async_api import Playwright, async_playwright, expect
async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    await context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # Open new page
    page = await context.new_page()
    # Go to https://erp.implementaconbubo.com/principal
    await page.goto("https://erp.implementaconbubo.com/")
    # Click [placeholder="Correo Electrónico"]
    await page.locator("[placeholder=\"Correo Electrónico\"]").click()
    # Fill [placeholder="Correo Electrónico"]
    await page.locator("[placeholder=\"Correo Electrónico\"]").fill("charly_alberti117@yahoo.com")
    # Click [placeholder="Contraseña"]
    await page.locator("[placeholder=\"Contraseña\"]").click()
    # Fill [placeholder="Contraseña"]
    await page.locator("[placeholder=\"Contraseña\"]").fill("TuGerente_2019!")
    # Click text=Ingresar
    await page.locator("text=Ingresar").click()
    await page.wait_for_url("https://erp.implementaconbubo.com/principal")
    await page.wait_for_timeout(3000)#3 SECONDS
    await page.screenshot(path="screenshots/Login1.png")

    # Click aside >> text=Ventas
    await page.locator("aside >> text=Ventas").click()
    await page.wait_for_timeout(3000)#3 SECONDS
    await page.wait_for_url("https://erp.implementaconbubo.com/pedido")
    # Click span:has-text("Cliente") >> nth=1
    await page.locator("span:has-text(\"Cliente\")").nth(1).click()
    await page.wait_for_timeout(3000)#3 SECONDS
    await page.wait_for_url("https://erp.implementaconbubo.com/cliente")
    await page.screenshot(path="screenshots/Cliente_Acceso.png")

    #Click text=+ Cliente
    await page.locator("text=+ Cliente").click()
    # Click div:nth-child(2) > div > .p-sidebar-close
    await page.locator("div:nth-child(2) > div > .p-sidebar-close").click()
    # Click button:has-text("Carga Masiva")
    await page.locator("button:has-text(\"Carga Masiva\")").click()
    # Click li:has-text("Carga masiva de clientes")
    await page.locator("li:has-text(\"Carga masiva de clientes\")").click()
    # Click button >> nth=1
    await page.frame_locator("body iframe").nth(2).locator("button").nth(1).click()
    # Click button:has-text("Carga Masiva")
    await page.locator("button:has-text(\"Carga Masiva\")").click()
    # Click text=Descargar el archivo de ejemplo
    async with page.expect_download() as download_info:
        async with page.expect_popup() as popup_info:
            await page.locator("text=Descargar el archivo de ejemplo").click()
        page1 = await popup_info.value
    download = await download_info.value
    # Close page
    await page1.close()
    # Click text=Exportar Lista a Excel
    await page.locator("text=Exportar Lista a Excel").click()
    # Click text=Aceptar
    await page.locator("text=Aceptar").click()
    await page.screenshot(path="screenshots/Cliente_BtnPrincipales.png")

    await context.tracing.stop(path="trace_BtnPrincipales.zip")
async def main() -> None:
     async with async_playwright() as playwright:
        await run(playwright) 

asyncio.run(main())
