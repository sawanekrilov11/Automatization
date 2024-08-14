from selenium.webdriver.common.by import By
from data import *

def test_shop(chrome_browser):
    chrome_browser.get(URL3)
    chrome_browser.find_element(By.ID, "user-name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome_browser.find_element(By.ID, "login-button").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    chrome_browser.find_element(By.ID, "shopping_cart_container").click()
    chrome_browser.find_element(By.ID, "checkout").click()
    chrome_browser.find_element(By.ID, "first-name").send_keys("Alex")
    chrome_browser.find_element(By.ID, "last-name").send_keys("Nekrylov")
    chrome_browser.find_element(By.ID, "postal-code").send_keys("185000")
    chrome_browser.find_element(By.ID, "continue").click()
    
    price = chrome_browser.find_element(By.CLASS_NAME, "summary_total_label")
    total = price.text.strip().replace("Total: $", "")

    except_total = "58.29"
    assert total == except_total
    print(f"Итоговая сумма равна ${total}")
