from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()

user_data_path = os.path.join(os.getcwd(), 'perfil')
options.add_argument(f'user-data-dir={user_data_path}')
options.page_load_strategy = "eager"
path_to_chrome_driver = r"chrome_driver\chromedriver.exe"
service = Service()
chrome = webdriver.Chrome(service=service, options=options)
chrome.get("https://jqueryui.com/draggable/")
action = ActionChains(chrome)
element = chrome.find_element(By.CSS_SELECTOR, "#content > p:nth-child(8)")

print(chrome.get_window_position())
chrome.set_window_position(0, 0)
sleep(1)
chrome.save_screenshot("./file_name.jpeg")


sleep(10)
chrome.quit()


css_selector_login = "#buttons > ytd-button-renderer > yt-button-shape > a"
btn_login = chrome.find_element(By.CSS_SELECTOR, css_selector_login)
btn_login.click()
input_login = chrome.find_element(By.ID, "identifierId")
input_login.clear()
input_login.send_keys("brunoalvesds1348@gmail.com")
css_selector_btn_env = "#identifierNext > div > button"
btn_env = chrome.find_element(By.CSS_SELECTOR, css_selector_btn_env)
btn_env.click()
text = chrome.find_element(
    By.CSS_SELECTOR, '#yDmH0d > c-wiz > div.aDGQwe > div.eKnrVb > div > div.j663ec > div > form > span > section > div > div > div > div:nth-child(2)')
chrome.switch_to.new_window()
print(text.get_property("innerHTML"))


sleep(20)
chrome.close()
