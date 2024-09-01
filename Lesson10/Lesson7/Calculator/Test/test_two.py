from Lesson7.Calculator.Pages.CMainPage import CCalculator
import allure

@allure.epic("Calculator")
@allure.title("Работа калькулятора")
@allure.description("Поиск полей, ввод данных, ожидание и вывод результата вычислений")
@allure.feature("Тест 2")
@allure.severity(severity_level='normal')

def test_calculator(chrome_browser):
    delay = 45
    result = 15
    keys_press = '7+8='
    with allure.step("Открытие калькулятора, ввод данных и ожидание результата"):
       ccalculator = CCalculator(chrome_browser)
       ccalculator.open()
       ccalculator.set_delay(delay)
       ccalculator.input_text(keys_press)
       ccalculator.wait_result(delay, result)

    with allure.step("Сравнение ФР с ОР"):
       assert ccalculator.result_text() == str(result)