import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/math.html')
data = browser.find_element_by_id('input_value').text

answer = browser.find_element_by_id('answer')
answer.send_keys(calc(data))

checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
checkbox.click()

radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
radiobutton.click()

submit = browser.find_element_by_css_selector('button.btn')
submit.click()
