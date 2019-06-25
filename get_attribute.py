import math
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/get_attribute.html')
data = browser.find_element_by_id('treasure').get_attribute('valuex')

answer = browser.find_element_by_id('answer')
answer.send_keys(calc(data))

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

radiobutton = browser.find_element_by_id('robotsRule')
radiobutton.click()

submit = browser.find_element_by_css_selector('button.btn')
submit.click()
