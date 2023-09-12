import unittest
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setUp")
class TestFlipkartWebSite(unittest.TestCase):
    # driver = webdriver.Chrome()
    # webdriver.WebDriver.get_
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.page = BasePage(self.driver)

    # @pytest.mark.skip
    def test_01_site_launch(self):
        self.driver.get("https://www.flipkart.com/")
        self.driver.implicitly_wait(2000)
        try:
            close_button = self.page.waitForElement('xpath', "//button[text()='✕']")
            close_button.click()
            self.driver.implicitly_wait(10000)
        except Exception as e:
            print('close button not found')
        finally:
            self.driver.implicitly_wait(5000)
            flikpart_text = self.page.waitForElement('class', "_2xm1JU").get_attribute('title')
            print(f'Image text :: {flikpart_text}')
            assert flikpart_text == 'Flipkart'

    # @pytest.mark.skip
    def test_02_search(self):
        self.driver.implicitly_wait(3000)
        search_ele = self.page.waitForElement('xpath', "//input[@type='text' and starts-with(@title, 'Search')]")
        search_ele.click()
        search_ele.send_keys('shoes')
        search_ele.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5000)
