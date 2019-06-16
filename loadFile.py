from selenium import webdriver
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, 'test.txt')

browser.get(link)
browser.find_element_by_css_selector('[name = "firstname"]').send_keys("Ivan")
browser.find_element_by_css_selector('[name = "lastname"]').send_keys("Ivanov")
browser.find_element_by_css_selector('[name = "email"]').send_keys("ivan@doma.net")
browser.find_element_by_id('file').send_keys(file_path)
browser.find_element_by_css_selector('button').click()
