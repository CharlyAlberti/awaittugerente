import asyncio
from playwright.async_api import Playwright, async_playwright, expect
async def run(playwright: Playwright) -> None:
    #CAMBIAR NOMBRE PARA AGREGAR UN CLIENTE NUEVO
    #EL Número de teléfono 
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
    # Click label:has-text("Agregar Nuevo")
    await page.locator("label:has-text(\"Agregar Nuevo\")").click()
    # Click text=Información de ClienteNombre del Cliente*Número de Teléfono:PhoneTipo de Documen >> [placeholder="Escriba el nombre o nit del cliente\."]
    await page.locator("text=Información de ClienteNombre del Cliente*Número de Teléfono:PhoneTipo de Documen >> [placeholder=\"Escriba el nombre o nit del cliente\\.\"]").click()
    # Fill text=Información de ClienteNombre del Cliente*Número de Teléfono:PhoneTipo de Documen >> [placeholder="Escriba el nombre o nit del cliente\."]
    await page.locator("text=Información de ClienteNombre del Cliente*Número de Teléfono:PhoneTipo de Documen >> [placeholder=\"Escriba el nombre o nit del cliente\\.\"]").fill("Agregar Cuenta PRUEBA")
    await page.wait_for_timeout(3000)#3 SECONDS
    await page.screenshot(path="screenshots/ModuloVentas1.png")
    # Click div[role="button"]
    await page.locator("div[role=\"button\"]").click()
    # Click text=México
    await page.locator("text=México").click()
    # Click [placeholder="Número de teléfono"]
    await page.locator("[placeholder=\"Número de teléfono\"]").click()
    # Fill [placeholder="Número de teléfono"]
    await page.locator("[placeholder=\"Número de teléfono\"]").fill("+52 222 339 3174")
    # Click text=Número De Identificación Tributaria
    await page.locator("text=Número De Identificación Tributaria").click()
    # Click li[role="option"]:has-text("Número De Identificación Tributaria")
    await page.locator("li[role=\"option\"]:has-text(\"Número De Identificación Tributaria\")").click()
    # Click #containerCliente span[role="listbox"] span >> nth=2
    await page.locator("#containerCliente span[role=\"listbox\"] span").nth(2).click()
    # Click #containerCliente span[role="listbox"] span >> nth=2
    await page.locator("#containerCliente span[role=\"listbox\"] span").nth(2).click()
    # Click input[name="addJuanInputName"] >> nth=1
    await page.locator("input[name=\"addJuanInputName\"]").nth(1).click()
    # Fill input[name="addJuanInputName"] >> nth=1
    await page.locator("input[name=\"addJuanInputName\"]").nth(1).fill("1234567890")
    # Click [placeholder="Escriba el Complemento del CI"]
    await page.locator("[placeholder=\"Escriba el Complemento del CI\"]").click()
    # Fill [placeholder="Escriba el Complemento del CI"]
    await page.locator("[placeholder=\"Escriba el Complemento del CI\"]").fill("1234567890")
    await page.wait_for_timeout(3000)#3 SECONDS
    await page.screenshot(path="screenshots/ModuloVentas2.png")
     # Click text=Guardar
    await page.locator("text=Guardar").click()
    await page.wait_for_timeout(3000)#3 SECONDS
    await page.screenshot(path="screenshots/ModuloVentas3.png")
    
    #ASSERTIONS
    assert await page.is_visible("text=Agregar Cuenta PRUEBA")
    await expect(page.locator("text=Agregar Cuenta PRUEBA")).to_be_visible()
    await page.screenshot(path="screenshots/ModuloVentas4.png")
    ##context.close()
    ##browser.close()
    
async def main() -> None:
     async with async_playwright() as playwright:
        await run(playwright) 

asyncio.run(main())