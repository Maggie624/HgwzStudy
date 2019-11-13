from appium import webdriver


class Driver:
    def __new__(cls, *args, **kwargs):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "SLA-AL00"
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = ".ui.LauncherUI"
        caps["autoGrantPermissions"] = "true"
        # caps['automationName'] = 'uiautomator2'
        caps['chromedriverExecutableDir'] = '/Users/maoqi/Public/tools/chromedriver/74/'
        caps['noReset'] = "true"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver


class WeChatDriver(Driver):
    # _instance = None
    _driver = None
    def __new__(cls, *args, **kwargs):
        if not WeChatDriver._driver:
            WeChatDriver._driver = super(WeChatDriver, cls).__new__(cls, *args, **kwargs)
        return WeChatDriver._driver



if __name__ == "__main__":
    a = WeChatDriver()


