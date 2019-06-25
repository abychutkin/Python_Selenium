import math
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

submit = browser.find_element_by_css_selector('.trollface')
submit.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

data = browser.find_element_by_id('input_value').text

input_field = browser.find_element_by_id('answer')
input_field.send_keys(calc(data))

submit = browser.find_element_by_css_selector('button.btn')
submit.click()
