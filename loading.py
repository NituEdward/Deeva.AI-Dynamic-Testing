import time
from selenium import webdriver

def test_site_loading_time():
    browser = webdriver.Chrome()  
    url = "https://www.deeva.ai/"  # Specificăm URL-ul

    start_time = time.time()  # Start timer

    # Deschidem URL-ul și maximizăm fereastra
    browser.get(url)
    browser.maximize_window()
    
    # Așteptăm ca pagina să fie complet încărcată
    browser.implicitly_wait(10)  

    # Măsurăm timpul de încărcare
    loading_time = time.time() - start_time
    print(f"Timpul de încărcare a paginii: {loading_time:.2f} secunde")

    browser.quit()

# Rulăm testul
test_site_loading_time()
