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
    await page.wait_for_timeout(30000)#30 SECONDS
    await page.screenshot(path="screenshots/ModuloVentas.png")
    # Click text=CLIENTE NUEVO 007
    
    # Click text=  Facturado
    await page.locator("text=Facturado/Efectivo/NIT 0").click()
    # Click Cerrar mensaje
    await page.locator("div[role=\"dialog\"] button").nth(2).click()
    # Click text= Recibo
    await page.locator("text=Recibo/Efectivo/NIT 0").click()
    # Click Cerrar mensaje
    await page.locator("div[role=\"dialog\"] button").nth(2).click()
    # Click text= Sin comprobante
    await page.locator("text=Sin comprobante/Efectivo/NIT 0").click()
    # Click Cerrar mensaje 
    await page.locator("button:has-text(\"Continuar\")").click()

    # Mensajes de Alerta
    await page.locator("text=Facturado/Efectivo/NIT 0").click()
    await page.screenshot(path="screenshots/ModuloVentas2.png")
    await page.wait_for_timeout(1000)#1 SECOND
    await page.locator("text=Recibo/Efectivo/NIT 0").click()
    await page.screenshot(path="screenshots/ModuloVentas3.png")
    await page.wait_for_timeout(1000)#1 SECOND
    await page.locator("text=Sin comprobante/Efectivo/NIT 0").click()
    await page.screenshot(path="screenshots/ModuloVentas4.png")
    await page.wait_for_timeout(1000)#1 SECOND
    ##context.close()
    ##browser.close()
    
async def main() -> None:
     async with async_playwright() as playwright:
        await run(playwright) 

asyncio.run(main())