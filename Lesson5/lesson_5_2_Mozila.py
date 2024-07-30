from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

mozila = webdriver.Firefox()

mozila.get("http://uitestingplayground.com/dynamicid")

add_button = mozila.find_element(
    By.XPATH, '//button[text()="Button with Dynamic ID"]').click()

count = 0
for x in range(3):
    add_button = mozila.find_element(
        By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    count = count + 1 
    sleep(3)
    print(count)

mozila.quit()