from selenium.webdriver.common.by import By
from helper.action import *
from pom.pom_api import *

def test_api(open_driver):
    click_elem(open_driver, btn_Access)
    click_elem(open_driver, btn_nprovider)
    wait(5)
    check_display(open_driver, color)