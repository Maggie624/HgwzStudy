from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium_po.page.main.xueqiu_page import XueqiuPage


class Driver:

    APP = "com.xueqiu.android"
    ACTIVITY = ".view.WelcomeActivityAlias"
    # ACTIVITY = '.common.MainActivity'

    def __new__(cls, *args, **kwargs) -> WebDriver:
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "Android Emulator"
        caps["appPackage"] = Driver.APP
        caps["appActivity"] = Driver.ACTIVITY
        caps["autoGrantPermissions"] = True
        caps['avd'] = 'Nexus_6P_API_29'
        caps['networkSpeed'] = 'full'
        caps['automationName'] = 'uiautomator2'
        # caps['dontStopAppOnReset'] = True       # 基于已经启动的APP执行脚本
        caps['noReset'] = True
        caps['ignoreUnimportantViews'] = True
        # caps['skipUnlock'] = True
        # caps['skipLogcatCapture'] = True
        # caps['disableAndroidWatchers'] = True
        caps['chromedriverExecutableDir'] = '/Users/maoqi/Public/tools/chromedriver/74/'
        caps['showChromedriverLog'] = True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver.implicitly_wait(10)

        return cls.driver


class XueqiuDriver(Driver):
    _driver = None
    def __new__(cls, *args, **kwargs):
        if not XueqiuDriver._driver:    # app未启动，则启动app
            print("首次启动app")
            XueqiuDriver._driver = super(XueqiuDriver, cls).__new__(cls, *args, **kwargs)
        else:       # app已启动，则设置app回到首页
            print("非首次启动app，回到雪球首页")
            # XueqiuDriver._driver.start_activity(Driver.APP, Driver.ACTIVITY)
            cls.driver.start_activity(Driver.APP, Driver.ACTIVITY)
        cls.xueqiu = XueqiuPage(cls.driver)
        cls.xueqiu.close_update().skip_ads().skip_tv().close_ib()
        WebDriverWait(cls.driver, 15, 0.5, ignored_exceptions=TimeoutException) \
            .until(EC.presence_of_element_located((By.XPATH, '//*[@text="雪球"]')))

        return XueqiuDriver._driver


if __name__ == "__main__":
    a = XueqiuDriver()
    xue = XueqiuPage(a)
    xue.goto_profile()
    b = XueqiuDriver()
    XueqiuPage(b).goto_trade()

