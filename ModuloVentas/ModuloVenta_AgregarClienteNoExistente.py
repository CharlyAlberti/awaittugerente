import asyncio
from playwright.async_api import Playwright, async_playwright, expect
async def run(playwright: Playwright) -> None:
    
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
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

    await page.wait_for_url("https://erp.implementaconbubo.com/principal")
    # Click #root >> text=Módulo Punto de Venta
    await page.locator("#root >> text=Módulo Punto de Venta").click()
    await page.wait_for_url("https://pos.implementaconbubo.com/principal")
    # Click text=Módulo Punto de Venta Vender >> button
    await page.locator("text=Módulo Punto de Venta Vender >> button").click()
    await page.wait_for_url("https://pos.implementaconbubo.com/venta")
    #await page.goto("https://pos.implementaconbubo.com/venta")
    await page.wait_for_timeout(50000)#50 SECONDS
    await page.screenshot(path="screenshots/ModuloVentas.png")
     # Click text=ClienteCambiar precio a todos los productos >> span >> nth=4
    await page.locator("text=ClienteCambiar precio a todos los productos >> span").nth(4).click()
    # Click label:has-text("Agregar Nuevo INEXISTENTE")
    # Click [placeholder="Escriba el nombre o nit del cliente\."]
    await page.locator("[placeholder=\"Escriba el nombre o nit del cliente\\.\"]").click()
    # Fill [placeholder="Escriba el nombre o nit del cliente\."]
    await page.locator("[placeholder=\"Escriba el nombre o nit del cliente\\.\"]").fill("Cliente01PRUEBA")
    await page.wait_for_timeout(3000)#3 SECONDS
    # Click [placeholder="Escriba el nombre o nit del cliente\."]
    await page.locator("[placeholder=\"Escriba el nombre o nit del cliente\\.\"]").click()
    await page.screenshot(path="screenshots/ModuloVentas1.png")
    #ASSERTIONS
    assert await page.is_visible("text=NO SE ENCONTRARON COINCIDENCIAS")
    await expect(page.locator("text=NO SE ENCONTRARON COIsNCIDENCIAS")).to_be_visible()
    await page.screenshot(path="screenshots/ModuloVentas2.png")
    ##context.close()
    ##browser.close()
    
async def main() -> None:
     async with async_playwright() as playwright:
        await run(playwright) 

asyncio.run(main())