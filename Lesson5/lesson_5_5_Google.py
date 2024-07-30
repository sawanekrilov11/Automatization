from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
chrome = webdriver.Chrome()
chrome.get("http://the-internet.herokuapp.com/inputs")
input_field = chrome.find_element(By.CSS_SELECTOR, "input")
input_field.send_keys("1000")
sleep(2)
input_field.clear()
sleep(2)
input_field.send_keys("999")
sleep(2)