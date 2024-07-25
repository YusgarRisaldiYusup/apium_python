import time
import pytest
from appium import webdriver
from helper.config import *


@pytest.fixture()
def open_driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '11.0',
        'deviceName': device_name,
        'app': Apk_path,
        'automationName': 'UiAutomator2'
    }

    direct = True

    driver = webdriver.Remote(host, desired_caps, direct_connection=direct)
    return driver

@pytest.fixture(scope='function', autouse=True)
def hook(request, open_driver):
    open_driver.implicitly_wait(3)
    time.sleep(2)
    yield
    open_driver.quit()


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # BEFORE SUITE

    yield
    # AFTER SUITE
