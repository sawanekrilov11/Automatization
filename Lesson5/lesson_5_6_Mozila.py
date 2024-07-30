from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
mozila = webdriver.Firefox()
mozila.get("https://the-internet.herokuapp.com/login")
input_name = mozila.find_element(By.ID, "username").send_keys("tomsmith")
sleep(2)
input_pass = mozila.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(2)
button = mozila.find_element(By.CSS_SELECTOR, "button").click()
sleep(1)