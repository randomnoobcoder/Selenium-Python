from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 20, poll_frequency=1,
                                  ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                      ElementNotSelectableException])

    def waitForElement(self, locatorType, locatorValue):
        element = None
        if locatorType == 'id':
            element = self.wait.until(EC.presence_of_element_located((By.ID, locatorValue)))
            return element
        elif locatorType == 'class':
            element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, locatorValue)))
            return element
        elif locatorType == 'xpath':
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, locatorValue)))
            return element
        elif locatorType == 'link_text':
            element = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, locatorValue)))
            return element
        elif locatorType == 'partial_link_text':
            element = self.wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, locatorValue)))
            return element
        else:
            return element

    def waitForElements(self, locatorType, locatorValue):
        element = None
        if locatorType == 'id':
            element = self.wait.until(EC.presence_of_all_elements_located((By.ID, locatorValue)))
            return element
        elif locatorType == 'class':
            element = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, locatorValue)))
            return element
        elif locatorType == 'xpath':
            element = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locatorValue)))
            return element
        elif locatorType == 'link_text':
            element = self.wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, locatorValue)))
            return element
        elif locatorType == 'partial_link_text':
            element = self.wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, locatorValue)))
            return element
        else:
            return element

    def waitForElementVisible(self, locatorType, locatorValue):
        element = None
        if locatorType == 'id':
            element = self.wait.until(EC.visibility_of_element_located((By.ID, locatorValue)))
            return element
        elif locatorType == 'class':
            element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locatorValue)))
            return element
        elif locatorType == 'xpath':
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locatorValue)))
            return element
        else:
            return element

    def waitForElementClickable(self, locatorType, locatorValue):
        element = None
        if locatorType == 'id':
            element = self.wait.until(EC.element_to_be_clickable((By.ID, locatorValue)))
            return element
        elif locatorType == 'class':
            element = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, locatorValue)))
            return element
        elif locatorType == 'xpath':
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locatorValue)))
            return element
        else:
            return element

