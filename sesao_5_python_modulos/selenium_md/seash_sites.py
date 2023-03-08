from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re


file_src_path = "srcs.txt"

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager"
chrome_options.add_argument("--start-maximized")

path_driver = os.path.join(os.getcwd(), "chrome_driver", "chromedriver.exe")

service = Service(executable_path=path_driver)

chrome = webdriver.Chrome(service=service, options=chrome_options)


with open(file_src_path, "r") as fl:
    regex = re.compile(r"[^\n]")
    for line in fl:
        if regex.search(line):
            chrome.get(line)
            sleep(2)
            chrome.switch_to.new_window()
