from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/find_xpath_form')

elements = browser.find_elements_by_tag_name('input')

for element in elements:
    element.send_keys('random text')

button = browser.find_element_by_xpath("//button[text()='Отправить']")
button.click()
