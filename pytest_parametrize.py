import time
import math
import pytest
from selenium import webdriver


def correct_answer():
    return math.log(int(time.time()))


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


lessons = ['236895', '236896', '236897', '236898', '236899', '236903',
           '236904', '236905']


@pytest.mark.parametrize('lesson', lessons)
def test_alien_messages(browser, lesson):
    url = 'https://stepik.org/lesson/{}/step/1'.format(lesson)
    browser.get(url)
    textarea = browser.find_element_by_tag_name('textarea')
    textarea.send_keys(str(correct_answer()))
    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()
    result = browser.find_element_by_css_selector('.smart-hints__hint')
    not_alien_message = 'Correct!'
    message = result.text
    assert message == not_alien_message, "Alien message is '{}'".format(message)
