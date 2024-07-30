from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
chrome = webdriver.Chrome()
chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range(5):
    add_button = chrome.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]').click()
delete_buttons = chrome.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
print(f"Размер списка кнопок Delete:{len(delete_buttons)}")
sleep(50)