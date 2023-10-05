from base.base_page import BasePage
import time
import unittest
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from base.base_page import BasePage
from selenium.webdriver.common.by import By


class Amazon:
    # driver = webdriver.WebDriver
    # window = driver.window_handles
    # driver.switch_to(window[1])
    # driver.switch_to(driver.current_window_handle)
    def __init__(self, driver):
        self.driver = driver
        self.page = BasePage(self.driver)

    def search_product(self, text):
        result = {}
        product_name = []
        product_asin = []
        product_price = []
        product_ratings = []
        product_ratings_num = []
        product_link = []
        search_box = self.page.waitForElement("id", "twotabsearchtextbox")
        search_box.click()
        search_box.send_keys(text, Keys.ENTER)
        self.driver.implicitly_wait(2000)
        result_list = self.driver.find_elements(By.XPATH,
                                                '//div[contains(@class, "s-result-item s-asin")]')  # //*[starts-with(@data-cel-widget, "search_result")]')
        for item in result_list:
            name = item.find_element(By.XPATH, './/span[@class="a-size-base-plus a-color-base a-text-normal"]')
            product_name.append(name.text)
            price = item.find_element(By.XPATH, './/span[@class="a-price-whole"]')
            product_price.append(price.text)
            result[name.text] = price.text
        filter_result = {k: v for k, v in result.items() if text in k.lower()}
        return result_list, filter_result

    def add_to_cart(self):
        ele_price = self.page.waitForElement("class", "priceToPay")
        price = ele_price.text  # get_attribute('data-price')
        ele_title = self.page.waitForElement('id', 'productTitle')
        product_title = ele_title.text
        self.page.waitForElement("id", "add-to-cart-button").click()
        return price, product_title

    def view_cart(self):
        self.page.waitForElement('id', 'nav-cart').click()
        item_title = self.page.waitForElement('class', 'sc-grid-item-product-title').text
        item_price = self.page.waitForElement('xpath', '//span[contains(@class,"sc-product-price")]').text
        return item_title, item_price
