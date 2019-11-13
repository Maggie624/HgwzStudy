from selenium.webdriver.common.by import By

from appium_po.common.base_page import BasePage


class DjRegisterPage(BasePage):
    _tel = (By.ID, 'et_telephone')     # 手机号
    _captcha = (By.ID, 'et_password')     # 校验码
    _login_btn = (By.ID, 'vg_login_btn')        # 登录

    def switch_to_danjuan_webview(self):
        self.driver.switch_to.context('WEBVIEW_com.xueqiu.android')
        return self

    def login(self, tel, captcha):
        self.find_and_sendkeys(self._tel, tel)
        self.find_and_sendkeys(self._captcha, captcha)
        self.find_and_click(self._login_btn)

