from Lesson7.Swag_labs.Pages.LoginPage import LoginPage
from Lesson7.Swag_labs.Pages.ProductPage import ProductPage
from Lesson7.Swag_labs.Pages.CheckoutPage import CheckoutPage
import allure

user_name = "standard_user"
password = "secret_sauce"

first_name = "Alex"
last_name = "Nekrylov"
postal_code = "185000"

sum = "$58.29"

@allure.epic("sausedemo")
@allure.title("Оформление заказа(в онлайн) магазине")
@allure.description("Оформление заказа, с выбором необходимого товара. Переход в корзину и сравниваем стоимость")
@allure.feature("Тест 3")
@allure.severity(severity_level='normal')
def test_shop(chrome_browser):
    with allure.step("Регистрация на странице сервиса"):
        login_page = LoginPage(chrome_browser)
        login_page.open()
        login_page.sign_in(user_name, password)
    
    with allure.step("Добавление товаров в корзину"):
        products_page = ProductPage(chrome_browser)
        products_page.add_to_cart()
        products_page.go_to_cart()
        products_page.checkout_click()

    with allure.step("Оформление заказа"):
        checkout_page = CheckoutPage(chrome_browser)
        checkout_page.make_checkout(first_name, last_name, postal_code)

    with allure.step("Сравнение Итоговой суммы(ФР) с ОР"):
        txt = checkout_page.check_total()
        assert sum in txt
    
        