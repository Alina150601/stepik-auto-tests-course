#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_class_name("btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    y = browser.find_element_by_id("input_value")
    x = int(y.text)
    rez = math.log(abs(12*math.sin(x)))
    input = browser.find_element_by_id("answer")
    input.send_keys(str(rez))
    button = browser.find_element_by_class_name("btn")
    button.click()
   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
