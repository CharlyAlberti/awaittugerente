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
    #Check text=Cliente GenericoSin asignar 1234567 , 7654321 , 2345678 0.00Sin Asignar >> input[type="checkbox"]
    await page.locator("text=Cliente GenericoSin asignar 1234567 , 7654321 , 2345678 0.00Sin Asignar >> input[type=\"checkbox\"]").check()
    # Check text=Juanito BananaSin asignar 2223393174 0.00Sin Asignar >> input[type="checkbox"]
    await page.locator("text=Juanito BananaSin asignar 2223393174 0.00Sin Asignar >> input[type=\"checkbox\"]").check()
    # Click text=Combinar Clientes
    await page.locator("text=Combinar Clientes").click()
    # Click text=Combinar ClientesMover Información de este cliente:Hacia este cliente:Combinar >> button
    await page.locator("text=Combinar ClientesMover Información de este cliente:Hacia este cliente:Combinar >> button").click()
    await page.wait_for_url("https://erp.implementaconbubo.com/cliente?")


    await context.tracing.stop(path="trace_CombinarCliente.zip")
async def main() -> None:
     async with async_playwright() as playwright:
        await run(playwright) 

asyncio.run(main())