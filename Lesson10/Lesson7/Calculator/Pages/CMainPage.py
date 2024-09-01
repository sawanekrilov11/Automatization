from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Lesson7.websait import URL2
import allure

class CCalculator:
    def __init__(self,browser):
        self.browser = browser

    @allure.step("Открываем страницу с калькулятором")
    def open(self):
        self.browser.get(URL2)

    @allure.step("Находим и заменяем в поле ввода значение")
    def set_delay(self, delay):
        delay_field = self.browser.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(delay)

    @allure.step("Ввод значений")
    def input_text(self, keys_calculator):
        for val in keys_calculator:
            self.browser.find_element(By.XPATH, f'//span[text()="{val}"]').click()
    
    @allure.step("Ожидание результата вычисления")
    def wait_result(self, delay, result):
        waiter = WebDriverWait(self.browser, delay +1)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), str(result)))

    @allure.step("Возвращение полученного результата в текстовом формате")
    def result_text(self):
        result = self.browser.find_element(By.CSS_SELECTOR, '.screen')
        return result.text