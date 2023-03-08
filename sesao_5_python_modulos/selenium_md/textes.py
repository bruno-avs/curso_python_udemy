from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

chrome_options = ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.page_load_strategy = "eager"

service = Service(ChromeDriverManager().install())

chrome = webdriver.Chrome(service=service, options=chrome_options)

chrome.get("https:\\www.google.com")
input = WebDriverWait(chrome, timeout=10).until(
    EC.presence_of_element_located((By.NAME, "q")), "erro")
input.send_keys("python", Keys.ENTER)

first_link = chrome.find_element(By.TAG_NAME, "h3")
first_link.click()

wait = WebDriverWait(chrome, timeout=3, poll_frequency=0.2)

element = chrome.find_element(By.ID, "id-search-field")


