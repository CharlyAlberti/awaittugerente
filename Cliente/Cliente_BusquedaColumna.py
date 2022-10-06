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

    
    await page.wait_for_timeout(50000)#40 SECONDS
    # Click text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type="text"] >> nth=0
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").first.click()
    # Fill text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type="text"] >> nth=0
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").first.fill("juanito banana")
    # Press Enter
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").first.press("Enter")
    # Fill text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type="text"] >> nth=0
    await page.wait_for_timeout(2000)#2 SECONDS
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").first.fill("")
    # Press Enter
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").first.press("Enter")
    await page.wait_for_timeout(2000)#2 SECONDS
    # Click text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type="text"] >> nth=1
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").nth(1).click()
    # Fill text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type="text"] >> nth=1
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").nth(1).fill("sin asignar")
    # Press Enter
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").nth(1).press("Enter")
    await page.wait_for_timeout(2000)#2 SECONDS
    # Fill text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type="text"] >> nth=1
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").nth(1).fill("")
    # Click text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type="text"] >> nth=2
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").nth(2).click()
    # Fill text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type="text"] >> nth=2
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").nth(2).fill("78945632")
    # Press Enter
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").nth(2).press("Enter")
    await page.wait_for_timeout(2000)#2 SECONDS
    # Fill text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type="text"] >> nth=2
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").nth(2).fill("")
    # Press Enter
    await page.locator("text=+ ClienteCarga MasivaExportar Lista a ExcelColumnasArrastre el título de una col >> input[type=\"text\"]").nth(2).press("Enter")
    await page.wait_for_timeout(2000)#3 SECONDS
    await page.screenshot(path="screenshots/BusquedaColumna.png")
    await context.tracing.stop(path="trace_Cliente_Busquedacolumna.zip")
async def main() -> None:
     async with async_playwright() as playwright:
        await run(playwright) 

asyncio.run(main())
