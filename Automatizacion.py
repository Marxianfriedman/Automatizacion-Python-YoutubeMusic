from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path="C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe",
        headless=False
    )
    page = browser.new_page()
    page.goto("https://music.youtube.com/")
    page.screenshot(path="brave_screenshot.png")

    # Para seleccionar la barra de busqueda
    search_input = page.locator("ytmusic-search-box input#input")
    search_input.click()
    print("Clic en la barra de busqueda")

    # Para insertar texto en la barra de busqueda
    page.locator("ytmusic-search-box input#input").fill("Moods - Love is Real")
    print("Se inserto texto en la barra de busqueda")

    # Busca 
    search_input.press("Enter")
    print("Se presiono ENTER")

    # Espera 3 segundos a que se recargue la pagina despues de la busqueda
    time.sleep(3)
    print("Esperando 3 segundos...")

    # Localiza y haz clic en el botón de reproducción del primer resultado
    play_button = page.locator('button.yt-spec-button-shape-next--filled:has-text("Reproducir")').first
    play_button.click()
    print("Se presiono el boton de play")

    # Espera 30 segundos miestras suena la cancion
    time.sleep(120)
    print("Esperando 30 segundos...")

    # Pausar - Versión mejorada que funciona en cualquier idioma
    pause_button = page.locator('[aria-label="Pausar"], [aria-label="Pause"]').first
    pause_button.click()
    print("Canción pausada")

    #=======================================================

   # SEGUNDA PESTAÑA (Usamos new_tab aquí)
    new_tab = browser.new_page()
    new_tab.goto("https://music.youtube.com")
    
    # Segunda canción (en la nueva pestaña)
    new_search = new_tab.locator("ytmusic-search-box input#input")
    new_search.click()
    new_search.fill("give you up (Darius remix)")
    new_search.press("Enter")
    time.sleep(3)
    new_tab.locator('button.yt-spec-button-shape-next--filled:has-text("Reproducir")').first.click()
    time.sleep(120)
    new_tab.locator('[aria-label="Pausar"], [aria-label="Pause"]').first.click()

    # give you up (Darius remix)


    input('Preciona ENTER para cerrar')
    browser.close() 

    
   