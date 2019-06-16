#!/usr/bin/env python
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

browser.get(link)
submit = browser.find_element_by_class_name("btn").click()
browser.switch_to.alert.accept()
x = browser.find_element_by_id("input_value")
x = x.text
y = calc(x)
answer = browser.find_element_by_id("answer")
answer.send_keys(y)
submit = browser.find_element_by_class_name("btn")
submit.click()
