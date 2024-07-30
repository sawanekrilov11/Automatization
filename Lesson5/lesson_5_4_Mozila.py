from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
mozila = webdriver.Firefox()
mozila.get("http://the-internet.herokuapp.com/entry_ad")
close_button = mozila.find_element(By.CSS_SELECTOR, ".modal-footer")
sleep(2)
close_button.click()
sleep(5)