from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Lesson7.websait import URL2

class CCalculator:
    def __init__(self,browser):
        self.browser = browser
        self.browser.get(URL2)

    def waiting_time(self):
        delay_input = self.browser.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(45)

    def click_button(self):
        self.browser.find_element(By.XPATH, "//span[text() = '7']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '+']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '8']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '=']").click()

    def waiting_button(self):
        WebDriverWait(self.browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        return self.browser.find_element(By.CLASS_NAME, "screen").text