from Lesson7.Swag_labs.Pages.SMainPage import SMainPage
from Lesson7.Swag_labs.Pages.Basket import Backet

def test_shop(chrome_browser):
    expect_total = "58.29"

    smainpage = SMainPage(chrome_browser)
    smainpage.data_fields()
    smainpage.add_to_cart()
    smainpage.click_add_to_cart()
    smainpage.go_to_cart()

    backet = Backet(chrome_browser)
    backet.checkout()
    backet.info()
    backet.price()
    
    assert expect_total in backet.price()
    print(f"Итоговая сумма равна ${backet.price()}")