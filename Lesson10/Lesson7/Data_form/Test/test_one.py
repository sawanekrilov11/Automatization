from Lesson7.Data_form.Pages.MainPage import MainPage
import allure
import pytest

values_dict = {
    'first-name': 'Иван',
    'last-name': 'Петров',
    'address': 'Ленина, 55-3',
    'e-mail': 'test@skypro.com',
    'phone': '+7985899998787',
    'zip-code': '',
    'city': 'Москва',
    'country': 'Россия',
    'job-position': 'QA',
    'company': 'SkyPro'
}

alert_danger_color = "rgba(248, 215, 218, 1)"
alert_success_color = "rgba(209, 231, 221, 1)"

fields_to_test_success = [
    key for key in values_dict.keys() if key != 'zip-code']

@allure.epic("Data types")
@allure.title("Заполнение формы")
@allure.description("Заполнение формы данными и проверка корректности введенных переменных")
@allure.feature("Тест 1")
@allure.severity(severity_level='normal')
@allure.step("Переход по ссылке и заполнение полей")
@pytest.fixture(scope="function")
def setup_form(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.open()
    main_page.fill_fields(values_dict)
    main_page.click_submit()
    return main_page

@allure.step("Сравнение цвета поля почтового индекса")
def test_alert_color(setup_form):
    color_zip = setup_form.find_element_property("zip-code")
    assert color_zip == alert_danger_color

@allure.step("Сравнение цвета остальных полей")
@pytest.mark.parametrize('selector', fields_to_test_success)
def test_success_color(setup_form, selector):
    color = setup_form.find_element_property(selector)
    assert color == alert_success_color

  


