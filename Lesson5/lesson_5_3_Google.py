from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
chrome = webdriver.Chrome()
chrome.get("http://uitestingplayground.com/classattr")
for x in range(3):
    blue_button = chrome.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    sleep(3)
    chrome.switch_to.alert.accept()
sleep(50)