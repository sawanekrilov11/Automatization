from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
chrome = webdriver.Chrome()
chrome.get("http://the-internet.herokuapp.com/entry_ad")
close_button = chrome.find_element(By.CSS_SELECTOR, ".modal-footer")
sleep(2)
close_button.click()
sleep(5)




