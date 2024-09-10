from selenium.webdriver.common.by import By
from Lesson7.websait import URL1
import allure

class MainPage:
    def __init__(self, browser, url = URL1):
        self.browser = browser
        self.url = url
    
    @allure.step("Открытие сервиса")
    def open(self):
        self.browser.get(self.url)

    @allure.step("Поиск и заполение полей")
    def fill_fields(self, v_dict: dict):
        for key, value in v_dict.items():
            selector = f'[name={key}]'
            self.browser.find_element(By.CSS_SELECTOR, selector).send_keys(value)

    @allure.step("Подтверждение заполнения полей")
    def click_submit(self):
        self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    @allure.step("Поиск полей и получение информации о значении цвета")
    def find_element_property(self, locator):
        background_color = self.browser.find_element(
            By.ID, locator).value_of_css_property("background-color")
        return background_color

        


    
    