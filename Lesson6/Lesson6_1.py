from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome = webdriver.Chrome()
wait = WebDriverWait(chrome, 30, 0.1)

chrome.get("http://uitestingplayground.com/ajax")

tap_button = chrome.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

text_content = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, ".bg-success"))).text

print(text_content)

chrome.quit()
