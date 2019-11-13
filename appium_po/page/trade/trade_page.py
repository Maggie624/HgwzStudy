import allure
from selenium.webdriver.common.by import By

from appium_po.common.base_page import BasePage
from appium_po.page.profile.danjuan_register_page import DjRegisterPage


class TradePage(BasePage):
    _hs = (By.ID, 'page_type_trade')    # 沪深，(MobileBy.ACCESSIBILITY_ID, 'page_type_trade')
    _gm = (By.ID, 'page_type_hk_us')    # 港美
    _fund = (By.ID, 'page_type_fund')    # 基金
    _btn_openaccount = (By.ID, 'btn_openaccount')       # 蛋卷基金安全开户，(MobileBy.ACCESSIBILITY_ID, '蛋卷基金安全开户')
    _performance = (By.ID, 'page_type_performance')     # 模拟
    _a_open_acount = (By.NAME, 'A股开户')        # A股开户
    _a_open_acount_btn = (By.XPATH, '//*[@text="A股开户"]/..')


    def goto_hs(self):
        with allure.step("点击沪深"):
            self.find_and_click(self._hs)
        with allure.step("等待'A股开户'按钮出现"):
            self.find(self._a_open_acount)
        return self

    def goto_gm(self):
        with allure.step("点击港美"):
            self.find_and_click(self._gm)
        return self

    def goto_fund(self):
        with allure.step("点击基金"):
            self.find_and_click(self._fund)
        return self

    def a_open_account(self):
        with allure.step("点击'A股开户'按钮"):
            self.find_and_click(self._a_open_acount_btn)
        return self

    def open_eggroll_account(self):
        with allure.step("点击'蛋卷基金安全开户'按钮"):
            self.find_and_click(self._btn_openaccount)
        return DjRegisterPage(self.driver)