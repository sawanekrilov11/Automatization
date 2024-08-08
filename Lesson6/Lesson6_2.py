from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get("http://uitestingplayground.com/textinput")

entry_field = chrome.find_element(
    "id", "newButtonName").send_keys("SkyPro")

tap_button = chrome.find_element(
    "id", "updatingButton").click()

update_button_name = chrome.find_element(
    "id", "updatingButton").text

print(update_button_name)

chrome.quit()
