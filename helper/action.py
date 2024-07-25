import time
from selenium.webdriver.common.by import By

def click_elem(open_driver, elem):
    open_driver.find_element(elem[0], elem[1]).click()


def check_display(open_driver, elem):
    open_driver.find_element(elem[0], elem[1]).is_displayed()


def wait(sec):
    time.sleep(sec)
