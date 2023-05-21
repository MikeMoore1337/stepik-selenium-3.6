import time

from selenium.webdriver.common.by import By


def test_add_to_cart_button_presence(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    add_to_cart_button = browser.find_element(By.XPATH,
                                              "/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/article[1]/div[1]/div[2]/form["
                                              "1]/button[1]")
    assert add_to_cart_button is not None, "Add to cart button is not present on the page"
