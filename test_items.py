import time

from selenium.webdriver.common.by import By


def test_add_to_cart_button_presence(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_button is not None, "Add to cart button is not present on the page"
