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
    await page.wait_for_timeout(40000)#40 SECONDS
    await page.screenshot(path="screenshots/ModuloVentas.png")

    # Click label:has-text("Delivery")
    await page.locator("label:has-text(\"Delivery\")").click()
    # Click div[role="dialog"] button
    await page.locator("div[role=\"dialog\"] button").click()
    # Click label:has-text("Delivery")
    await page.locator("label:has-text(\"Delivery\")").click()
    # Click div[role="dialog"] button
    await page.locator("div[role=\"dialog\"] button").click()
    # Click label:has-text("Delivery")
    await page.locator("label:has-text(\"Delivery\")").click()
    # Click div[role="dialog"] span >> nth=4
    await page.locator("div[role=\"dialog\"] span").nth(4).click()
    # Click text=Pedidos Ya
    await page.locator("text=Pedidos Ya").click()
    await page.wait_for_timeout(1000)#1 SECONDS
    await page.screenshot(path="screenshots/PedidosYa.png")
    # Click label:has-text("Pedidos Ya")
    await page.locator("label:has-text(\"PedidosYa\")").click()
    # Click text=Seleccione delivery:Pedidos Ya >> span >> nth=3
    await page.locator("text=Seleccione delivery:Pedidos Ya >> span").nth(3).click()
    # Click text=Patio Service
    await page.locator("text=Patio Service").click()
    await page.wait_for_timeout(1000)#1 SECONDS
    await page.screenshot(path="screenshots/Patio Service.png")
    # Click label:has-text("Patio Service")
    await page.locator("label:has-text(\"PatioService\")").click()
    # Click text=Seleccione delivery:Patio Service >> span >> nth=3
    await page.locator("text=Seleccione delivery:Patio Service >> span").nth(3).click()
    # Click text=Uber Eats
    await page.locator("text=Uber Eats").click()
    await page.wait_for_timeout(1000)#1 SECONDS
    await page.screenshot(path="screenshots/UberEats.png")
    # Click label:has-text("Uber Eats")
    await page.locator("label:has-text(\"Uber Eats\")").click()
    # Click text=Seleccione delivery:Uber Eats >> span >> nth=4
    await page.locator("text=Seleccione delivery:Uber Eats >> span").nth(4).click()
    # Click text=Mr. Delivery
    await page.locator("text=Mr. Delivery").click()
    await page.wait_for_timeout(1000)#1 SECONDS
    await page.screenshot(path="screenshots/MrDelicery.png")
    # Click label:has-text("Mr. Delivery")
    await page.locator("label:has-text(\"Mr. Delivery\")").click()
    # Click text=Seleccione delivery:Mr. Delivery >> span >> nth=4
    await page.locator("text=Seleccione delivery:Mr. Delivery >> span").nth(4).click()
    # Click text=Yaigo
    await page.locator("text=Yaigo").click()
    await page.wait_for_timeout(1000)#1 SECONDS
    await page.screenshot(path="screenshots/Yiago.png")
    # Click label:has-text("Yaigo")
    await page.locator("label:has-text(\"Yaigo\")").click()
    # Click text=Seleccione delivery:Yaigo >> span >> nth=4
    await page.locator("text=Seleccione delivery:Yaigo >> span").nth(4).click()
    # Click text=Otro
    await page.locator("text=Otro").click()
    await page.wait_for_timeout(1000)#1 SECONDS
    await page.screenshot(path="screenshots/Otro.png")
    # Click label:has-text("Otro")
    await page.locator("label:has-text(\"Otro\")").click()
    # Click text=Seleccione delivery:Otro >> span >> nth=4
    await page.locator("text=Seleccione delivery:Otro >> span").nth(4).click()
    # Click text=WhatsApp
    await page.locator("text=WhatsApp").click()
    await page.wait_for_timeout(1000)#1 SECONDS
    await page.screenshot(path="screenshots/WhatsApp.png")
    # Click label:has-text("WhatsApp")
    await page.locator("label:has-text(\"WhatsApp\")").click()
    # Click text=Seleccione delivery:WhatsApp >> span >> nth=4
    await page.locator("text=Seleccione delivery:WhatsApp >> span").nth(4).click()
     # Click text=Seleccione delivery:WhatsApp >> button
    await page.locator("text=Seleccione delivery:WhatsApp >> button").click()

    ##context.close()
    ##browser.close()
    
async def main() -> None:
     async with async_playwright() as playwright:
        await run(playwright) 

asyncio.run(main())