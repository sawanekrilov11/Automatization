from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome = webdriver.Chrome()
wait = WebDriverWait(chrome, 30, 0.1)

chrome.get(" https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

attribute_name = chrome.find_element(By.ID, "award").get_attribute("src")

print(attribute_name)

chrome.quit()


