from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
chrome = webdriver.Chrome()
chrome.get("http://uitestingplayground.com/dynamicid")
add_button = chrome.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
count = 0
for x in range(3):
    add_button = chrome.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    count = count + 1 
    sleep(3)
    print(count)

sleep(50)