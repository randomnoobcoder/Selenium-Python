import pytest
from tests.base_test import BaseTestAmazon
from base.base_page import BasePage
from common.amazon_common import Amazon


# @pytest.mark.usefixtures("setUp_amazon")
class TestAmazon(BaseTestAmazon):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.page = BasePage(self.driver)
        self.amazon = Amazon(self.driver)

    @pytest.mark.skip
    def test_site_launch(self):
        title = self.driver.title
        print(title)
        assert "Amazon.in" in title

    @pytest.mark.skip
    def test_search(self):
        result_list, result = self.amazon.search_product("shoes")
        print(f'Result Dictionary : {result}')
        for key, value in result.items():
            assert "shoes" in key.lower()

    def test_add_to_cart(self):
        result_list, result = self.amazon.search_product("shoes")
        item_selected = list(result.keys())[1]
        print(f'Item Selected : {item_selected}')
        self.page.waitForElement('xpath', f'//*[text()="{item_selected}"]').click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        price, item_name = self.amazon.add_to_cart()
        print(f'Product added is : {item_name}')
        print(f'Price of added product is : {price}')
        item_title, item_price = self.amazon.view_cart()
        print(f'Product in Bag : {item_title}')
        print(f'Price product in Bag : {item_price}')

