from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.base_page import BasePage
from appium_po.page.optional_page import OptionalPage
from appium_po.page.search_page import SearchPage


class XueqiuPage(BasePage):
    _myProfile = (By.ID, 'user_profile_icon')       # 主页中"我的"icon
    _optional_tab = (By.XPATH, '//*[@text="自选"]')
    _xueqiu_tab = (By.XPATH, '//*[@text="雪球"]')



    def __init__(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "android emulator"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        # caps['automationName'] = 'uiautomator2'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 15, 0.5, ignored_exceptions=TimeoutException)\
            .until(EC.presence_of_element_located((By.ID, 'home_search')))


    def goto_search(self):
        self.driver.find_element_by_id('home_search').click()
        return SearchPage(self.driver)

    def goto_profile(self):
        self.find_and_click(self._myProfile)
        from appium_po.page.profile_page import ProfilePage
        return ProfilePage(self.driver)

    def goto_optional(self):
        ele = self.find(self._optional_tab, min_y_per=0.95)
        ele.click()
        return OptionalPage(self.driver).close_defalut_tip()

    def goto_xueqiu(self):
        ele = self.find(self._xueqiu_tab, min_y_per=0.95)
        ele.click()
        return XueqiuPage()

    def get_default(self):
        """推荐"""
        return False

    def get_ads(self):
        return False
