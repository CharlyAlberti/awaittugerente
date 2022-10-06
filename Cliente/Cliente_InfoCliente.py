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
    await page.wait_for_timeout(5000)#5 SECONDS
    await page.wait_for_url("https://erp.implementaconbubo.com/pedido")
    # Click span:has-text("Cliente") >> nth=1
    await page.locator("span:has-text(\"Cliente\")").nth(1).click()
    await page.wait_for_timeout(3000)#3 SECONDS
    await page.wait_for_url("https://erp.implementaconbubo.com/cliente")
    await page.screenshot(path="screenshots/Cliente_Acceso.png")

    # Click text=+ Cliente
    await page.locator("text=+ Cliente").click()
    # Click [placeholder="Escriba el nombre del cliente"]
    await page.locator("[placeholder=\"Escriba el nombre del cliente\"]").click()
    # Fill [placeholder="Escriba el nombre del cliente"]
    await page.locator("[placeholder=\"Escriba el nombre del cliente\"]").fill("Cliente Generico")
    # Click input[name="discount"]
    await page.locator("input[name=\"discount\"]").click()
    # Fill input[name="discount"]
    await page.locator("input[name=\"discount\"]").fill("10")
    # Click [placeholder="Escriba el correo"]
    await page.locator("[placeholder=\"Escriba el correo\"]").click()
    # Fill [placeholder="Escriba el correo"]
    await page.locator("[placeholder=\"Escriba el correo\"]").fill("cuentagenerica@gmail.com")
    # Click [placeholder="Escriba el nombre del contacto"]
    await page.locator("[placeholder=\"Escriba el nombre del contacto\"]").click()
    # Fill [placeholder="Escriba el nombre del contacto"]
    await page.locator("[placeholder=\"Escriba el nombre del contacto\"]").fill("contacto generico")
    # Click [placeholder="Número de teléfono"] >> nth=0
    await page.locator("[placeholder=\"Número de teléfono\"]").first.click()
    # Fill [placeholder="Número de teléfono"] >> nth=0
    await page.locator("[placeholder=\"Número de teléfono\"]").first.fill("+591 123 4567")
    # Click [placeholder="Número de teléfono"] >> nth=1
    await page.locator("[placeholder=\"Número de teléfono\"]").nth(1).click()
    # Fill [placeholder="Número de teléfono"] >> nth=1
    await page.locator("[placeholder=\"Número de teléfono\"]").nth(1).fill("+591 765 4321")
    # Click [placeholder="Número de teléfono"] >> nth=2
    await page.locator("[placeholder=\"Número de teléfono\"]").nth(2).click()
    # Fill [placeholder="Número de teléfono"] >> nth=2
    await page.locator("[placeholder=\"Número de teléfono\"]").nth(2).fill("+591 234 5678")
    # Click [placeholder="Escriba la razon social para la factura"]
    await page.locator("[placeholder=\"Escriba la razon social para la factura\"]").click()
    # Fill [placeholder="Escriba la razon social para la factura"]
    await page.locator("[placeholder=\"Escriba la razon social para la factura\"]").fill("Ventas en General")
    # Click input[name="nit"]
    await page.locator("input[name=\"nit\"]").click()
    # Fill input[name="nit"]
    await page.locator("input[name=\"nit\"]").fill("1234567890")
    # Click input[name="ci_complement"]
    await page.locator("input[name=\"ci_complement\"]").click()
    # Fill input[name="ci_complement"]
    await page.locator("input[name=\"ci_complement\"]").fill("1234567890")
    await page.screenshot(path="screenshots/InfoCliente.png")
    await page.wait_for_timeout(3000)#3 SECONDS
     # Click main >> text=Registrar
    await page.locator("main >> text=Registrar").click()
    await context.tracing.stop(path="trace_Cliente_InfoCliente.zip")
    
    
async def main() -> None:
     async with async_playwright() as playwright:
        await run(playwright) 

asyncio.run(main())