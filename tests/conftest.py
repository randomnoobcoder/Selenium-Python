import os
import time
from selenium import webdriver
import pytest

from driver.driver import Driver


@pytest.fixture(scope='class')
def setUp_flipkart(request):
    driver = Driver.get_driver('chrome')
    driver.maximize_window()
    driver.set_window_size(1920, 1080)
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(3)
    driver.delete_all_cookies()
    driver.quit()


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def setUp_meta(request):
    if request.param == "chrome":
        driver = Driver.get_driver('chrome')
        driver.maximize_window()
        driver.get("https://www.meta.com/portal/")
        if request.cls is not None:
            request.cls.driver = driver
        yield driver
        time.sleep(3)
        driver.delete_all_cookies()
        driver.quit()
    if request.param == "firefox":
        driver = Driver.get_driver('firefox')
        driver.get("https://www.meta.com/portal/")
        if request.cls is not None:
            request.cls.driver = driver
        yield driver
        time.sleep(3)
        driver.delete_all_cookies()
        driver.quit()
# @pytest.fixture(scope='class')
# def setUp_meta(request):
#     driver = Driver.get_driver('firefox')
#     driver.maximize_window()
#     driver.get("https://www.meta.com/portal/")
#     if request.cls is not None:
#         request.cls.driver = driver
#     yield driver
#     time.sleep(3)
#     driver.delete_all_cookies()
#     driver.quit()


@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def init_driver(request):
    if request.params == 'chrome':
        web_driver = webdriver.ChromeService(
            executable_path=os.path.join(os.getcwd(), os.path.abspath("../browsers/chromedriver/chromedriver.exe")))
    if request.params == 'firefox':
        web_driver = webdriver.ChromeService(
            executable_path=os.path.join(os.getcwd(), os.path.abspath('../browsers/geckodriver/geckodriver.exe')))
    request.cls.driver = web_driver
