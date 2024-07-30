from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

mozila = webdriver.Firefox()

mozila.get("http://uitestingplayground.com/classattr")

for x in range(3):
    blue_button = mozila.find_element(
        By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    sleep(3)
    mozila.switch_to.alert.accept()

mozila.quit()