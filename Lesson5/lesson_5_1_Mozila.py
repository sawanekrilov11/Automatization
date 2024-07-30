from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

mozila = webdriver.Firefox()

mozila.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range(5):
    add_button = mozila.find_element(
        By.CSS_SELECTOR, '[onclick="addElement()"]').click()
    
    delete_buttons = mozila.find_elements(
        By.CSS_SELECTOR, '[onclick="deleteElement()"]')

print(f"Размер списка кнопок Delete:{len(delete_buttons)}")

mozila.quit()