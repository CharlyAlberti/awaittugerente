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
     # Click text=Realizar venta con:
   
     # Click #ProdFav div >> nth=1
    await page.locator("#ProdFav div").nth(1).click()
    # Click [id="\32 47079"] >> nth=0
    await page.locator("[id=\"\\32 47079\"]").first.click()
    # Click [id="\31 571"] div >> nth=1
    await page.locator("[id=\"\\31 571\"] div").nth(1).click()
    # Click [id="\31 915"]
    await page.locator("[id=\"\\31 915\"]").click()
    # Click [id="\35 04097"] >> nth=0
    await page.locator("[id=\"\\35 04097\"]").first.click()
    # Click [id="\31 8092"] div >> nth=1
    await page.locator("[id=\"\\31 8092\"] div").nth(1).click()
    # Click [id="\31 7983"] div:has-text("WALTHER")
    await page.locator("[id=\"\\31 7983\"] div:has-text(\"WALTHER\")").click()
    # Click [id="\32 44509"] >> nth=0
    await page.locator("[id=\"\\32 44509\"]").first.click()
    # Click [id="\31 0067"] div >> nth=1
    await page.locator("[id=\"\\31 0067\"] div").nth(1).click()
    # Click [id="\31 915"] div:has-text("Sin asignar")
    await page.locator("[id=\"\\31 915\"] div:has-text(\"Sin asignar\")").click()
    # Click [id="\32 44626"] >> nth=0
    await page.locator("[id=\"\\32 44626\"]").first.click()
    # Click [id="\31 8093"] div >> nth=1
    await page.locator("[id=\"\\31 8093\"] div").nth(1).click()
    # Click [id="\31 7985"] div:has-text("NORTH AMERICAN ARMS")
    await page.locator("[id=\"\\31 7985\"] div:has-text(\"NORTH AMERICAN ARMS\")").click()
    # Click [id="\32 44537"] >> nth=0
    await page.locator("[id=\"\\32 44537\"]").first.click()
    # Click [id="\31 8091"] div >> nth=1
    await page.locator("[id=\"\\31 8091\"] div").nth(1).click()
    # Click [id="\31 7981"] div:has-text("ANSCHUTZ")
    await page.locator("[id=\"\\31 7981\"] div:has-text(\"ANSCHUTZ\")").click()
    # Click [id="\32 44382"] >> nth=0
    await page.locator("[id=\"\\32 44382\"]").first.click()
    # Click [id="\31 8136"] div >> nth=1
    await page.locator("[id=\"\\31 8136\"] div").nth(1).click()
    # Click [id="\31 915"] div:has-text("Sin asignar")
    await page.locator("[id=\"\\31 915\"] div:has-text(\"Sin asignar\")").click()
    # Click [id="\32 44994"] >> nth=0
    await page.locator("[id=\"\\32 44994\"]").first.click()
    # Click [id="\31 844"] div >> nth=1
    await page.locator("[id=\"\\31 844\"] div").nth(1).click()
    # Click [id="\31 7981"] div:has-text("ANSCHUTZ")
    await page.locator("[id=\"\\31 7981\"] div:has-text(\"ANSCHUTZ\")").click()
    # Click [id="\32 45089"] >> nth=0
    await page.locator("[id=\"\\32 45089\"]").first.click()
    await page.wait_for_timeout(3000)#3 SECONDS
    await page.screenshot(path="screenshots/ModuloVentas2.png")
    # Click text=Pagar64,221.00 >> nth=0
    await page.locator("text=Pagar64,221.00").first.click()
    await page.wait_for_timeout(3000)#3 SECONDS
#ASSERTIONS ASERCIÓN DE PRECIO 
    assert await page.is_visible("text=64,221.00")
    await expect(page.locator("text=64,221.00 >> nth=1")).to_be_visible()
    await page.screenshot(path="screenshots/ModuloVentas3.png")

    # Click .k-icon >> nth=0
    await page.locator(".k-icon").first.click()
    # Click li[role="option"]:has-text("CLIENTE NUEVO 007")
    await page.locator("li[role=\"option\"]:has-text(\"CLIENTE NUEVO 007\")").click()
    await page.screenshot(path="screenshots/ModuloVentas4.png")
    await page.wait_for_timeout(3000)#3 SECONDS
#ASSERTIONS ASERCIÓN DEl CLIENTE 
    assert await page.is_visible("text=RAZON SOCIAL: CLIENTE NUEVO 007")
    await expect(page.locator("text=RAZON SOCIAL: CLIENTE NUEVO 007")).to_be_visible()
    assert await page.is_visible("text=NIT: 1046599551")
    await expect(page.locator("text=NIT: 1046599551")).to_be_visible()
    ##assert await page.is_visible("text=Teléfono: +591 54654654")
    ##await expect(page.locator("text=Teléfono: +591 54654654")).to_be_visible()
    await page.wait_for_timeout(3000)#3 SECONDS
    
    await context.tracing.stop(path="trace_ModuloPOS.zip")
    
async def main() -> None:
     async with async_playwright() as playwright:
        await run(playwright) 

asyncio.run(main())