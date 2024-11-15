from importuri import *

#Setup pentru Browser
@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

# TC_001
def test_website_status(browser):
    url = "https://www.deeva.ai/"
    response = requests.get(url)
    # Verificarea codului de status HTTP
    assert response.status_code == 200, f"Codul de status este {response.status_code}, dar asteptam 200"
    # Verificarea lungimii raspunsului
    assert len(response.text) > 0, "Continutul raspunsului este gol"

#TC_002
def test_choose_deeva(browser):
    url = "https://www.deeva.ai/"
    browser.get(url)
    browser.maximize_window()

    time.sleep(2)

    click_deeva = browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div/div/div[1]/div[2]/div[2]/a")
    click_deeva.click()

    time.sleep(2)

    welcome_to_deeva = browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/button")
    assert welcome_to_deeva.is_displayed() , "Pagina nu a fost redirectionata catre selectie"
    

#TC_003
def test_login(browser):
    url ="https://www.deeva.ai/"
    browser.get(url)
    browser.maximize_window()

    login = browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div/div/header/div/div[3]/div/a[2]")
    login.click()

    time.sleep(3)

    email = browser.find_element(By.ID,"email")
    email_login = "eddieinquieries@gmail.com"
    email.send_keys(email_login)
    assert email.is_displayed(), "Campul pentru email nu este vizibil"

    time.sleep(1)

    password = browser.find_element(By.ID,"password")
    password_login = "!Deeva123"
    password.send_keys(password_login)
    assert password.is_displayed(), "Campul pentru parolă nu este vizibil"

    time.sleep(1)

    login = browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/div[2]/div/form/button")
    login.click()
    assert login.is_displayed(), "Butonul de login nu este vizibil"
    
    time.sleep(10)

#TC_004
def test_AI(browser):
    url ="https://www.deeva.ai/"
    browser.get(url)
    browser.maximize_window()

    login = browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div/div/header/div/div[3]/div/a[2]")
    login.click()

    time.sleep(3)

    email = browser.find_element(By.ID,"email")
    email_login = "eddieinquieries@gmail.com"
    email.send_keys(email_login)
    assert email.is_displayed(), "Campul pentru email nu este vizibil"

    time.sleep(1)

    password = browser.find_element(By.ID,"password")
    password_login = "!Deeva123"
    password.send_keys(password_login)
    assert password.is_displayed(), "Campul pentru parolă nu este vizibil"

    time.sleep(1)

    login = browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/div[2]/div/form/button")
    login.click()
    assert login.is_displayed(), "Butonul de login nu este vizibil"
    
    time.sleep(3)

    message_input = browser.find_element(By.NAME,"userInput")
    message = "Hello Deeva , how are you today?"
    message_input.send_keys(message)
    message_input.send_keys(Keys.RETURN)

    time.sleep(3)

    send = browser.find_element(By.XPATH,"/html/body/div/div[3]/div/div[2]/div[5]/form/div/div/div/div/button[1]")
    send.click()

    time.sleep(10)

    mesaj = "last-message-div"
    mesaj = browser.find_element(By.CLASS_NAME,mesaj)

    assert mesaj.is_displayed() , "Chat-ul nu functioneaza"

    time.sleep(15)


#TC05
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

    # Adăugăm o aserțiune opțională, dacă vrei să limitezi timpul de încărcare
    assert loading_time < 5, "Site-ul s-a încărcat prea lent!"

    browser.quit()



