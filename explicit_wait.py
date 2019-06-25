import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

button = browser.find_element_by_id('book')
WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR'))
button.click()

input_field = browser.find_element_by_id('answer')
data = browser.find_element_by_id('input_value').text
input_field.send_keys(calc(data))

submit_button = browser.find_element_by_id('solve')
submit_button.click()
