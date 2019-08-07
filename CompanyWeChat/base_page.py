from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element_by_wait(self, by, locator):
        element = WebDriverWait(self.driver, 5, 0.5, ignored_exceptions=TimeoutException)\
            .until(EC.presence_of_element_located((by, locator)))
        return element

    def find_elements_by_wait(self, by, locator, timeout=5):
        elements = WebDriverWait(self.driver, timeout, 0.5, ignored_exceptions=TimeoutException)\
            .until(EC.visibility_of_all_elements_located((by, locator)))
        return elements

    def find_element_invisibility(self, by, locator):
        WebDriverWait(self.driver, 5, 0.5).until(EC.invisibility_of_element_located((by, locator)))

    def click_by_js(self, by, locator):
        WebDriverWait(self.driver, 5, 0.5, ignored_exceptions=TimeoutException)\
            .until(EC.element_to_be_clickable((by, locator)))
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(by, locator))

    def click_and_check(self, target, expect):
        def click_and_find(x):
            self.click_by_js(*target)
            length = self.find_elements_by_wait(*expect, timeout=1.5)
            return len(length) >= 1
        WebDriverWait(self.driver, 6, 0.5, ignored_exceptions=TimeoutException).until(click_and_find)

    def click_by_sele(self, by, locator):
        element = WebDriverWait(self.driver, 5, 0.5, ignored_exceptions=TimeoutException)\
            .until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def sendKeys(self, by, locator, msg, isclean=True):
        element = self.find_element_by_wait(by, locator)
        if isclean:
            element.clear()
        element.send_keys(msg)

    def refresh(self):
        self.driver.refresh()


if __name__ == "__main__":
    chrome = webdriver.Chrome()
    chrome.get('https://baidu.com')
    driver = BasePage(chrome)
    driver.find_element_by_wait(By.LINK_TEXT, '张艺兴')