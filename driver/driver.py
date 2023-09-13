from selenium import webdriver
import os
from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.firefox.options import Options


class Driver:
    @staticmethod
    def get_driver(browser_name):
        driver = None
        if browser_name == 'chrome':
            # options = webdriver.ChromeOptions()
            # options.add_argument("--headless")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            # print('\n', os.getcwd())
            # exe_path = os.path.join(os.getcwd(), os.path.abspath("../browsers/chromedriver/chromedriver.exe"))
            # print(f'\n Chrome Path : {exe_path}')
            # service = ChromeService(executable_path=exe_path)
            # driver = webdriver.Chrome(service=service)
        elif browser_name == 'firefox':
            driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()))
            # exe_path = os.path.join(os.getcwd(), os.path.abspath('../browsers/geckodriver/geckodriver.exe'))
            # print(f'\n FireFox Path : {exe_path}')
            # service = FireFoxService(executable_path=exe_path)
            # # options = Options()
            # # options.binary_location = exe_path
            # driver = webdriver.Firefox(service=service)
        return driver
