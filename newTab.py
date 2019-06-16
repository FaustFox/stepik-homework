from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
button = browser.find_element_by_class_name("trollface")
button.click()
window = browser.window_handles[1]
browser.switch_to.window(window)
x = browser.find_element_by_id("input_value")
x = x.text
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_class_name("btn").click()
