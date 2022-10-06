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
    await page.wait_for_timeout(3000)#5 SECONDS
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

    # Click text=Juanito BananaSin asignar 2223393174 0.00Sin Asignar >> span >> nth=4
    await page.locator("text=Juanito BananaSin asignar 2223393174 0.00Sin Asignar >> span").nth(4).click()
    # Click text=Frío
    await page.locator("text=Frío").click()
    # Click text=CLIENTE NUEVO 007Sin asignar 4454456788 , 646488 , 11100000 0.00Sin Asignar >> span >> nth=4
    await page.locator("text=CLIENTE NUEVO 007Sin asignar 4454456788 , 646488 , 11100000 0.00Sin Asignar >> span").nth(4).click()
    # Click text=Tibio
    await page.locator("text=Tibio").click()
    # Click text=NUEVA EMPRESA SACSin asignar 654123655 , 951952321 0.00Sin Asignar >> span >> nth=4
    await page.locator("text=NUEVA EMPRESA SACSin asignar 654123655 , 951952321 0.00Sin Asignar >> span").nth(4).click()
    # Click text=Caliente
    await page.locator("text=Caliente").click()
    # Click text=fa sin emailSin asignar 0.00Sin Asignar >> span >> nth=4
    await page.locator("text=fa sin emailSin asignar 0.00Sin Asignar >> span").nth(4).click()
    # Click ul[role="listbox"] >> text=Frío
    await page.locator("ul[role=\"listbox\"] >> text=Frío").click()
    # Click text=fa emailSin asignar 0.00Sin Asignar >> span >> nth=4
    await page.locator("text=fa emailSin asignar 0.00Sin Asignar >> span").nth(4).click()
    # Click ul[role="listbox"] >> text=Tibio
    await page.locator("ul[role=\"listbox\"] >> text=Tibio").click()
    # Click text=Gabriela CalvimontesSin asignar +59179823705 0.00Sin Asignar >> span >> nth=3
    await page.locator("text=Gabriela CalvimontesSin asignar +59179823705 0.00Sin Asignar >> span").nth(3).click()
    # Click ul[role="listbox"] >> text=Caliente
    await page.locator("ul[role=\"listbox\"] >> text=Caliente").click()
    # Click text=Gabriela SuarezSin asignar 78945632 0.00Sin Asignar >> span >> nth=4
    await page.locator("text=Gabriela SuarezSin asignar 78945632 0.00Sin Asignar >> span").nth(4).click()
    # Click ul[role="listbox"] >> text=Frío
    await page.locator("ul[role=\"listbox\"] >> text=Frío").click()
    # Click div:has-text("Cargando...") >> nth=2
    await page.locator("div:has-text(\"Cargando...\")").nth(2).click()
    # Click text=Arizona GonzalesSin asignar 76014141 0.00Sin Asignar >> span >> nth=3
    await page.locator("text=Arizona GonzalesSin asignar 76014141 0.00Sin Asignar >> span").nth(3).click()
    # Click ul[role="listbox"] >> text=Caliente
    await page.locator("ul[role=\"listbox\"] >> text=Caliente").click()
    # Click text=Gloria RiberaSin asignar 0.00Sin Asignar >> span >> nth=3
    await page.locator("text=Gloria RiberaSin asignar 0.00Sin Asignar >> span").nth(3).click()
    # Click ul[role="listbox"] >> text=Frío
    await page.locator("ul[role=\"listbox\"] >> text=Frío").click()
    # Click span[role="listbox"]:has-text("Sin Asignar")
    await page.locator("span[role=\"listbox\"]:has-text(\"Sin Asignar\")").click()
    # Click ul[role="listbox"] >> text=Tibio
    await page.locator("ul[role=\"listbox\"] >> text=Tibio").click()
    await page.screenshot(path="screenshots/CambiarPrioridad.png")


    await context.tracing.stop(path="trace_Cliente_InfoCliente.zip")

    # EXPECT Message  
    context.close()
    browser.close()
    
async def main() -> None:
     async with async_playwright() as playwright:
        await run(playwright) 

asyncio.run(main())
