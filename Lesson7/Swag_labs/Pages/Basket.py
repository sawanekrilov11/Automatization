from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Backet:
    def __init__(self, browser):
        self.browser = browser
    
    def checkout(self):
        self.check = (By.ID, "checkout")
        self.browser.find_element(*self.check).click()

    def info(self):
        self.first_name = (By.ID, "first-name")
        self.browser.find_element(*self.first_name).send_keys("Alexander")
        self.last_name = (By.ID, "last-name")
        self.browser.find_element(*self.last_name).send_keys("Nekrylov")
        self.postcode = (By.ID, "postal-code")
        self.browser.find_element(*self.postcode).send_keys("185000")
        self.continue_button = (By.ID, "continue")
        self.browser.find_element(*self.continue_button).click()

    def price(self):
        WebDriverWait(self.browser, 40, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
        total_price = self.browser.find_element(By.CSS_SELECTOR, ".summary_total_label")
        total = total_price.text.strip().replace("Total: $","")
        return total