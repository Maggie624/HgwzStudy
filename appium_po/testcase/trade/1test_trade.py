import allure
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.driver.xueqiu import XueqiuDriver
from appium_po.page.main.xueqiu_page import XueqiuPage
from appium_po.page.profile.danjuan_register_page import DjRegisterPage
from appium_po.page.trade.trade_page import TradePage


class TestTrade:
    def setup_class(self):
        self.driver = XueqiuDriver()
        self.xueqiu = XueqiuPage(self.driver)
        self.trade = TradePage(self.driver)
        self.danjuan_register = DjRegisterPage(self.driver)

    @allure.story("A股开户")
    def test_a_open(self):
        self.xueqiu.goto_trade().goto_hs()
        self.trade.a_open_account()

    @allure.story("蛋卷基金")
    def test_danjuan_open(self):
        self.xueqiu.goto_trade().goto_fund().open_eggroll_account()


    def test_webview(self):
        self.xueqiu.goto_trade()
        print(self.driver.page_source, end='========不带webview=======')      # 返回不带webview的组件树
        for i in range(10):
            print(self.driver.contexts, end='maomao_contexts\n')
        WebDriverWait(self.driver, 10, 1).until(lambda x: "WEBVIEW_com.xueqiu.android" in self.driver.contexts)
        print(self.driver.page_source, end='========带webview=======\n')       # 返回带有webview的组件树，可以使用原生定位去定位webview内的元素
        self.driver.switch_to.context("WEBVIEW_com.xueqiu.android")
        print(self.driver.page_source, end='========返回html=======\n')   # 返回html,可用selenium定位其中的内容

    def test_001(self):
        self.xueqiu.goto_trade().goto_fund().open_eggroll_account()
        # print(self.driver.page_source, end='========不带webview=======')  # 返回不带webview的组件树
        for i in range(10):
            print(self.driver.contexts)
            # if 'WEBVIEW_com.xueqiu.android' in self.driver.contexts:
            #     break
        # self.danjuan_register.switch_to_danjuan_webview()
        print(self.danjuan_register.driver.context, end='current=========\n')
        self.danjuan_register.login('17612128888', '1234')
        # print(self.danjuan_register.driver.page_source)

