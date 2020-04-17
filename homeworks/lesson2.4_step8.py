from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    wait = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element_by_id('book')
    button.click()

    browser.execute_script("window.scrollBy(0, 100);")

    # посчитать число
    elem_x = browser.find_element_by_id('input_value')
    x = elem_x.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    sub = browser.find_element_by_id('solve')
    sub.click()




finally:


    # закрываем браузер после всех манипуляций
    browser.quit()


