from selenium import webdriver

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)

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

