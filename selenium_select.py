from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects2.html')

num1 = int(browser.find_element_by_id('num1').text)
num2 = int(browser.find_element_by_id('num2').text)

select = Select(browser.find_element_by_id('dropdown'))
select.select_by_value(str(num1+num2))

submit = browser.find_element_by_css_selector('button.btn')
submit.click()
