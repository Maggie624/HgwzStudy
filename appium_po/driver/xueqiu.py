from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium_po.config.config import *
import shelve
import pickle
from appium_po.page.base_page import BasePage
from appium_po.page.xueqiu_page import XueqiuPage


# def save_driver(obj):
#     with shelve.open(temp_save) as fp:
#         fp['driver'] = obj
#
# def get_driver():
#     with shelve.open(temp_save) as fp:
#         try:
#             print('maomao  getdriver11111\n')
#             driver = fp['driver']
#         except KeyError:
#             print('maomao  createdriver22222\n')
#             return XueqiuDriver().driver
#     print('maomao  33333\n')
#     return driver

# def save_driver(obj):
#     with open(temp_save, 'wb') as fp:
#          pickle.dump(obj, fp)
#
# def get_driver():
#     while True:
#         try:
#             with open(temp_save, 'rb') as fp:
#                 try:
#                     print('maomao  getdriver11111\n')
#                     driver = pickle.load(fp)
#                 except EOFError:
#                     fp.close()
#                 else:
#                     return driver
#         except FileNotFoundError:
#             print('maomao  createdriver22222\n')
#             return XueqiuDriver().driver

class Driver:
    def __new__(cls, *args, **kwargs):
        print('Create a new driver', end='maomao\n')
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "Android Emulator"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps['automationName'] = 'uiautomator2'

        print('11111\n')
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

        cls.xueqiu = XueqiuPage(cls.driver)
        print('maomao  44444\n')
        cls.xueqiu.skip_ads().skip_tv().close_ib()

        WebDriverWait(cls.driver, 15, 0.5, ignored_exceptions=TimeoutException) \
            .until(EC.presence_of_element_located((By.ID, 'home_search')))
        return cls.driver


class XueqiuDriver(Driver):
    # _instance = None
    _driver = None
    def __new__(cls, *args, **kwargs):
        print('Xueqiu Driver', end='maomao\n')
        if not XueqiuDriver._driver:
            print('777777', end='maomao\n')
            XueqiuDriver._driver = super(XueqiuDriver, cls).__new__(cls, *args, **kwargs)
        print('8888888', end='maomao\n')
        return XueqiuDriver._driver



if __name__ == "__main__":
    a = XueqiuDriver()
    xue = XueqiuPage(a)
    xue.goto_profile()

