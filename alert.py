import math
from selenium import webdriver 


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

submit = browser.find_element_by_css_selector('button.btn')
submit.click()

alert = browser.switch_to.alert
alert.accept()

data = browser.find_element_by_id('input_value').text
input_field = browser.find_element_by_id('answer')
input_field.send_keys(calc(data))

submit = browser.find_element_by_css_selector('button.btn')
submit.click()
