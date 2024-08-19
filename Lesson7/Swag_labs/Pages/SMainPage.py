from selenium.webdriver.common.by import By
from Lesson7.websait import URL3

class SMainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(URL3)

    def data_fields(self):
        self._name = (By.ID, "user-name")
        self._pass = (By.ID, "password")
        self._log_button = (By.ID, "login-button")
        self.browser.find_element(*self._name).send_keys("standard_user")
        self.browser.find_element(*self._pass).send_keys("secret_sauce")
        self.browser.find_element(*self._log_button).click()

    def add_to_cart(self):
        self.Sauce_Labs_Backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.Sauce_Labs_Bolt_TShirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.Sauce_Labs_Onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

    def click_add_to_cart(self):
        self.browser.find_element(*self.Sauce_Labs_Backpack).click()
        self.browser.find_element(*self.Sauce_Labs_Bolt_TShirt).click()
        self.browser.find_element(*self.Sauce_Labs_Onesie).click()

    def go_to_cart(self):
        self.cart = (By.ID, "shopping_cart_container")
        self.browser.find_element(*self.cart).click()