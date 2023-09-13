import time
import unittest
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from common.meta_cart import MetaCart
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setUp_meta")
class TestMetaShop(BaseTest):  # unittest.TestCase):
    # driver = webdriver.WebDriver

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.page = BasePage(self.driver)
        self.car_page = MetaCart(self.driver)

    # @pytest.mark.skip
    def test_00_site_launch(self):
        title = self.driver.title
        print(title)
        assert "Meta Store" in title and "Meta Portal" in title
        meta_text = self.page.waitForElementVisible('xpath',
                                                    "//img[@class = 'xx3o462 x13dflua x11xpdln']").get_attribute("alt")
        print(f'meta_text : {meta_text}')
        assert "Meta" in meta_text
        # self.assertEqual(meta_text, "Meta")

    @pytest.mark.skip
    def test_01_check_items_availability(self):
        ele_TV = self.page.waitForElement('xpath', "//*[text()='TV']")
        # action = ActionChains(self.driver)
        # action.move_to_element(ele_TV).perform()
        self.driver.execute_script("arguments[0].scrollIntoView();", ele_TV)
        availability_text = self.page.waitForElement('xpath',
                                                     '//*[@id="explore"]/div[2]/div/div[4]/div/div/div[1]/div/div[3]/div[1]/div/div/div/span')
        print(availability_text.text)
        self.assertEqual(availability_text.text, 'Not available')

    @pytest.mark.skip
    def test_02_open_new_window(self):
        print(f'First Window Title: {self.driver.title}')
        # Moving to YT link
        yt_link = self.driver.find_element(By.XPATH, "(//*[@class='x2e0w50'])[4]")  # look nth child
        action = ActionChains(self.driver)
        action.move_to_element(yt_link).perform()
        time.sleep(3)
        yt_link.click()
        # Checking opened window
        windows = self.driver.window_handles
        print(windows)
        # Switch to YT window
        self.driver.switch_to.window(windows[1])
        self.driver.implicitly_wait(5)
        print(f'Second Window Title: {self.driver.title}')
        yt_channel = self.page.waitForElement('class', "ytd-channel-name")
        self.assertEqual(yt_channel.text, "Meta")
        # Switching back to Meta windows
        self.driver.switch_to.window(windows[0])
        assert 'Meta Store' in self.driver.title

    @pytest.mark.skip
    def test_03_cart(self):
        self.car_page.add_product_to_cart('Meta Quest 2')
        self.car_page.add_product_to_cart('Meta Quest Pro')
        self.car_page.view_bag()
        # all_items = []
        # added_items = self.driver.find_elements(By.XPATH, '//*[contains(@class, "x1a4ywym xobpncf ")]')
        # for item in added_items:
        #     print(all_items.append(item.text))
        # assert 'Quest 2' in all_items and 'Quest Pro' in all_items

        total_price_calculated = self.car_page.calc_total_product_price()
        total_price_displayed = self.car_page.total_price_displayed()
        self.assertEqual(total_price_calculated, total_price_displayed)

        # actions = ActionChains(self.driver)
        # product_list = self.page.waitForElement('xpath', '//*[text()="Meta Quest"]')
        # actions.move_to_element(product_list).perform()  # hover cursor over Meta Quest to display all items
        # print('Selecting Quest 2')
        # self.page.waitForElement('xpath', "//*[text()='Meta Quest 2']").click()  # selecting Meta Quest 2
        # print('Selected Quest 2')
        # time.sleep(5)
        # buy_now_1 = self.page.waitForElement('xpath', '(//*[@role="button"])[10]')  # BUY NOW button
        # print('Moving to BUY NOW button')
        # actions.move_to_element(buy_now_1).perform()  # moving to BUY NOW button
        # # self.driver.execute_script("arguments[0].scrollIntoView();", buy_now_1)
        # print('Moved to BUY NOW button and clicking')
        # self.driver.implicitly_wait(2000)
        # buy_now_1.click()
        # print('clicked')
        # # self.driver.execute_script("return document.readyState")
        # print('Selecting 128GB')
        # product_size = self.page.waitForElement('xpath', '(//*[@role="radio"])[5]')  # selecting 128GB
        # product_size.click()
        # print('clicked')
        # self.driver.implicitly_wait(2000)
        # print('clicking Buy now')
        # self.page.waitForElement('xpath', '(//*[@role="button" and @aria-busy="false"])[17]').click()  # Buy now click
        # print('clicked')
        # self.driver.implicitly_wait(2000)
        # print('clicking Continue')
        # self.page.waitForElement('xpath', '//*[starts-with(@aria-label, "Continue")]').click()
        # print('clicked')
        # print('clicking Bag')
        # self.page.waitForElement('partial_link_text', 'bag').click()  # click on bag
        # print('clicked')
        # time.sleep(5)
        # print('checking Bag item')
        # added_item = self.page.waitForElement('xpath', '//*[contains(@class, "x1a4ywym xobpncf ")]')
        # assert "Meta Quest 2" in added_item.text

    @pytest.mark.skip
    def test_04_screenshot(self):
        meta_log = self.page.waitForElement('xpath', '(//img[@class="xx3o462 x13dflua x11xpdln"])[1]')
        # self.driver.find_element().screenshot_as_png
        with open("logo.png", 'wb') as file:
            file.write(meta_log.screenshot_as_png)
