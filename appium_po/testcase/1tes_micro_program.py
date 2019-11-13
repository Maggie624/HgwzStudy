import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.driver.wechat import WeChatDriver
from appium_po.page.wechat_page import WeChatPage
import time

class TestMicro:
    def setup_class(self):
        self.driver = WeChatDriver()
        self.wechat = WeChatPage(self.driver)

    def test_01_login(self):
        self.wechat.find_and_click((By.XPATH, '//*[@text="文件传输助手"]'))
        self.wechat.find_and_click((By.XPATH, '//*[@text="雪球股票"]'))

        ele = self.wechat.find((By.CLASS_NAME, 'android.widget.Image'), timeout=15)
        for i in range(20):
            time.sleep(2)
            print(i, end='maomao-i\n')
            print(self.wechat.driver.contexts)
            if 'WEBVIEW_com.tencent.mm:tools' in self.wechat.driver.contexts:
                self.wechat.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
                print('switch ok!')
        ele.click()
        self.wechat.find_and_sendkeys((By.CLASS_NAME, 'android.widget.EditText'), 'alibaba')
        self.wechat.find_and_click((By.XPATH, '//*[@text="阿里巴巴"]'))