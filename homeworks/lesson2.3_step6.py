from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # кликнуть на кнопку
    button = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button.click()

    # переключаемся на новую вкладку
    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    #посчитать число
    elem_x = browser.find_element_by_id('input_value')
    x = elem_x.text
    y = calc(x)

    # ввести ответ
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

