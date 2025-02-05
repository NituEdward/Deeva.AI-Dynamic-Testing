from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
import requests

# Constants
class TestData:
    BASE_URL = "https://www.deeva.ai/"
    EMAIL = "eddieinquieries@gmail.com"
    PASSWORD = "!Deeva123"
    CHAT_MESSAGE = "Hello Deeva, how are you today?"

# Page Objects
class LoginPage:
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_LINK = (By.XPATH, "//a[contains(@href, '/login')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, email, password):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK)).click()
        self.wait.until(EC.presence_of_element_located(self.EMAIL_FIELD)).send_keys(email)
        self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

class ChatPage:
    MESSAGE_INPUT = (By.NAME, "userInput")
    SEND_BUTTON = (By.XPATH, "//button[@type='submit']")
    WELCOME_MESSAGE = (By.XPATH, "//button[contains(@class, 'welcome')]")
    CHOOSE_DEEVA_BUTTON = (By.XPATH, "//a[contains(@href, '/choose-deeva')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def send_message(self, message):
        message_field = self.wait.until(EC.presence_of_element_located(self.MESSAGE_INPUT))
        message_field.send_keys(message)
        self.wait.until(EC.element_to_be_clickable(self.SEND_BUTTON)).click()

    def choose_deeva(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_DEEVA_BUTTON)).click()
        return self.wait.until(EC.presence_of_element_located(self.WELCOME_MESSAGE))

# Fixtures
@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

# Test Cases
def test_website_status():
    """Verifică disponibilitatea și răspunsul website-ului Deeva.ai"""
    response = requests.get(TestData.BASE_URL)
    assert response.status_code == 200, f"Status code invalid: {response.status_code}"
    assert len(response.text) > 0, "Răspunsul este gol"

def test_choose_deeva(browser):
    """Verifică funcționalitatea de selectare Deeva"""
    browser.get(TestData.BASE_URL)
    chat_page = ChatPage(browser)
    welcome_element = chat_page.choose_deeva()
    assert welcome_element.is_displayed(), "Elementul de welcome nu este vizibil"

def test_login(browser):
    """Verifică funcționalitatea de autentificare"""
    browser.get(TestData.BASE_URL)
    login_page = LoginPage(browser)
    login_page.login(TestData.EMAIL, TestData.PASSWORD)
    
    # Verificăm că suntem logați așteptând elementul de chat
    chat_page = ChatPage(browser)
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(chat_page.MESSAGE_INPUT)
    ), "Login nereușit"

def test_chat_functionality(browser):
    """Verifică funcționalitatea de chat cu Deeva"""
    browser.get(TestData.BASE_URL)
    login_page = LoginPage(browser)
    chat_page = ChatPage(browser)
    
    login_page.login(TestData.EMAIL, TestData.PASSWORD)
    chat_page.send_message(TestData.CHAT_MESSAGE)
    
    # Așteptăm să apară răspunsul (poți adăuga verificări specifice pentru răspuns)
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'message-response')]"))
    )

