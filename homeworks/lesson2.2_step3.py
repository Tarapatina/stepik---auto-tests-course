from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    first_el = browser.find_element_by_id('num1')
    first = first_el.text

    second_el = browser.find_element_by_id('num2')
    second = second_el.text

    def calc():
        sum = str(int(first) + int(second))
        return sum

    a = calc()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(a)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

