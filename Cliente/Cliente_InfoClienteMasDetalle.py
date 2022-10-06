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
     # Click div[role="treeitem"] span >> nth=2
    await page.locator("div[role=\"treeitem\"] span").nth(2).click()
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

     # Click .k-content > .row > div > .k-form-field > div > .k-widget > .k-dropdown-wrap > .k-select > .k-icon >> nth=0
    await page.locator(".k-content > .row > div > .k-form-field > div > .k-widget > .k-dropdown-wrap > .k-select > .k-icon").first.click()
    # Click text=Comerciante
    await page.locator("text=Comerciante").click()
    # Click .k-content > .row > div:nth-child(2) > .k-form-field > div > .k-widget > .k-dropdown-wrap > .k-select > .k-icon
    await page.locator(".k-content > .row > div:nth-child(2) > .k-form-field > div > .k-widget > .k-dropdown-wrap > .k-select > .k-icon").click()
    # Click text=ZONA NORTE
    await page.locator("text=ZONA NORTE").click()
    # Click [placeholder="Escriba el código del cliente"]
    await page.locator("[placeholder=\"Escriba el código del cliente\"]").click()
    # Fill [placeholder="Escriba el código del cliente"]
    await page.locator("[placeholder=\"Escriba el código del cliente\"]").fill("01234567890")
    await page.locator("input[role=\"spinbutton\"]").click()
    # Fill input[role="spinbutton"]
    await page.locator("input[role=\"spinbutton\"]").fill("13/08/1994")
    # Click [placeholder="Escriba la dirección"]
    await page.locator("[placeholder=\"Escriba la dirección\"]").click()
    # Fill [placeholder="Escriba la dirección"]
    await page.locator("[placeholder=\"Escriba la dirección\"]").fill(" Av. Bolivia, El Alto, Bolivia")
    # Click text=Forma PagoTarjetaTiempo Entrega >> input[type="tel"]
    await page.locator("text=Forma PagoTarjetaTiempo Entrega >> input[type=\"tel\"]").click()
    # Fill text=Forma PagoTarjetaTiempo Entrega >> input[type="tel"]
    await page.locator("text=Forma PagoTarjetaTiempo Entrega >> input[type=\"tel\"]").fill("20")
    # Click text=Días CreditoForma EntregaCliente recoge >> input[type="tel"]
    await page.locator("text=Días CreditoForma EntregaCliente recoge >> input[type=\"tel\"]").click()
    # Fill text=Días CreditoForma EntregaCliente recoge >> input[type="tel"]
    await page.locator("text=Días CreditoForma EntregaCliente recoge >> input[type=\"tel\"]").fill("5")
    # Click [placeholder="Escriba la ciudad"]
    await page.locator("[placeholder=\"Escriba la ciudad\"]").click()
    # Fill [placeholder="Escriba la ciudad"]
    await page.locator("[placeholder=\"Escriba la ciudad\"]").fill("El Alto")
    # Click input[name="business_name"]
    await page.locator("input[name=\"business_name\"]").click()
    # Fill input[name="business_name"]
    await page.locator("input[name=\"business_name\"]").fill("polleria")
    # Click [placeholder="Escriba un comentario"]
    await page.locator("[placeholder=\"Escriba un comentario\"]").click()
    # Fill [placeholder="Escriba un comentario"]
    await page.locator("[placeholder=\"Escriba un comentario\"]").fill("prueba")
    await page.wait_for_timeout(3000)#3 SECONDS
    await page.screenshot(path="screenshots/InfoClienteMasDetalle.png")
    await context.tracing.stop(path="trace_Cliente_InfoClienteMasDetalle.zip")
    
    
async def main() -> None:
     async with async_playwright() as playwright:
        await run(playwright) 

asyncio.run(main())