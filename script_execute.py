import math
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome();
browser.get('https://SunInJuly.github.io/execute_script.html')
data = browser.find_element_by_id('input_value').text

input_field = browser.find_element_by_id('answer')
input_field.send_keys(calc(data))

checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
checkbox.click()

browser.execute_script('button = document.getElementsByTagName("button")[0]; button.scrollIntoView();')

radiobutton = browser.find_element_by_id('robotsRule')
radiobutton.click()

submit = browser.find_element_by_css_selector('button.btn')
submit.click()
