from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # кликнуть на кнопку
    button = browser.find_element_by_css_selector(".btn")
    button.click()

    # принять alert
    alert = browser.switch_to.alert
    alert.accept()

    # решить уровнение
    elem_x = browser.find_element_by_id('input_value')
    x = elem_x.text
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    # нажать на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

