from Lesson7.Calculator.Pages.CMainPage import CCalculator

def test_calculator(chrome_browser):
    ccalculator = CCalculator(chrome_browser)
    ccalculator.waiting_time()
    ccalculator.click_button()
    assert "15" in ccalculator.waiting_button()