from selenium import webdriver
import time
import math
from math import log, sin
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elem_x = browser.find_element_by_id('input_value')
    x = elem_x.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    button = browser.find_element_by_id("answer")
    button.send_keys(y)

    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()