import time
from base.base_page import BasePage


class MetaCart:
    def __init__(self, driver):
        self.driver = driver
        self.page = BasePage(self.driver)

    def add_product_to_cart(self, product):
        product_list = self.page.waitForElement('xpath', '//*[text()="Meta Quest"]')
        self.page.actions.move_to_element(product_list).perform()  # hover cursor over Meta Quest to display all items
        print(f'Selecting {product}')
        self.page.waitForElement('xpath', f'//*[text()="{product}"]').click()  # selecting Meta Quest 2
        print(f'Selected {product}')
        print(f'Waiting 5 sec .....')
        time.sleep(5)
        if product == 'Meta Quest 2':
            buy_now_1 = self.page.waitForElement('xpath', '(//*[@role="button"])[10]')  # BUY NOW button
        else:
            buy_now_1 = self.page.waitForElement('xpath', '(//*[@role="button"])[11]')
        print('Moving to BUY NOW button')
        # self.page.actions.move_to_element(buy_now_1).perform()  # moving to BUY NOW button
        self.driver.execute_script("arguments[0].scrollIntoView();", buy_now_1)
        `print('Moved to BUY NOW button and clicking')
        print(f'Waiting 3 sec .....')
        time.sleep(3)
        buy_now_1.click()
        print('clicked')
        # self.driver.execute_script("return document.readyState")
        if product == 'Meta Quest 2':
            print('Selecting 128GB')
            self.page.waitForElement('xpath', '(//*[@role="radio"])[5]').click()  # selecting 128GB
            # product_size.click()
            print('clicked')
            print(f'Waiting 3 sec .....')
            time.sleep(3)
            self.driver.implicitly_wait(5000)
            print('clicking Buy now')
            self.page.waitForElement('xpath', '(//*[@role="button" and @aria-busy="false"])[17]').click()  # Buy now click
            print('clicked')
        self.driver.implicitly_wait(2000)
        print('clicking Continue')
        self.page.waitForElement('xpath', '//*[starts-with(@aria-label, "Continue")]').click()
        print('clicked')
        print(f'Waiting 2 sec .....')
        time.sleep(2)
        print('Clicking Close button')
        self.page.waitForElement('xpath', '//*[@aria-label="Close"]').click()
        print('clicked')
        # print('clicking Bag')
        # self.waitForElement('partial_link_text', 'bag').click()  # click on bag
        # print('clicked')
        print(f'Waiting 1 sec .....')
        time.sleep(1)

    def view_bag(self):
        self.driver.get("https://www.meta.com/bag/")
        # self.waitForElement('xpath', '//*[@aria-label="View bag items"]').click()
        time.sleep(2)

    def calc_total_product_price(self):
        price_list = []
        prices = self.page.waitForElements('xpath',
                                      '//*[contains(@class, "xeuugli x2lwn1j x78zum5 xdt5ytf xozqiw3 x1r0jzty x2lah0s")]')
        for price in prices:
            a = price.text.replace('$', '')
            price_list.append(a)
        print(price_list)
        total_price = [float(price) for price in price_list if price != '']
        # Ways of scrolling
        #     self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)/7);")
        #     self.driver.execute_script("argument[0].scrollIntoView();", price)
        total_sum = sum(total_price)
        print(f'Total price calculated : {total_sum}')
        return total_sum

    def total_price_displayed(self):
        total_price_ele = self.page.waitForElement('xpath', '(//*[contains(@class, "xeuugli x2lwn1j x78zum5 x1qughib")])[8]')
        a = total_price_ele.text.split('$')[1]
        total_price_displayed = a[:a.index(',')] + a[a.index(',') + 1:]
        print(f'Total Price Displayed : {float(total_price_displayed)}')
        return float(total_price_displayed)
