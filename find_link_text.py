import math
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/find_link_text')
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = browser.find_element_by_link_text(link_text)
link.click()

name = browser.find_element_by_name('first_name')
name.send_keys('Aleksey')
surname = browser.find_element_by_name('last_name')
surname.send_keys('Bychutkin')
city = browser.find_element_by_class_name('city')
city.send_keys('Zhytomir')
country = browser.find_element_by_id('country')
country.send_keys('Ukraine')
submit = browser.find_element_by_class_name('btn-default')
submit.click()
