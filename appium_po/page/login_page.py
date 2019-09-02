from selenium.webdriver.common.by import By

from appium_po.page.base_page import BasePage
from appium_po.page.profile_page import ProfilePage


class LoginPage(BasePage):
    _phone = (By.ID, 'iv_login_phone')      # 手机号
    _username = (By.ID, 'login_account')        # 用户名
    _psw = (By.ID, 'login_password')        # 密码
    _login_btn = (By.ID, 'button_next')     # 登录
    _loginMsg = (By.ID, 'md_content')       # 登录失败信息
    _loginMsg_cofirm = (By.ID, 'md_buttonDefaultPositive')      # 登录失败弹窗，确认按钮
    _iv_action_back = (By.ID, 'iv_action_back')     # 取消登录
    _leave = (By.ID, 'md_buttonDefaultNegative')    # 狠心离开

    def login(self, username, psw):
        self.find_and_sendkeys(self._username, username)
        self.find_and_sendkeys(self._psw, psw)
        self.find_and_click(self._login_btn)
        return self

    def login_msg(self):
        ele = self.find(self._loginMsg)
        return ele.text

    def close_msg(self):
        self.find_and_click(self._loginMsg_cofirm)
        return self

    def goto_profile(self):
        self.find_and_click(self._iv_action_back)
        self.find_and_click(self._leave)
        return ProfilePage(self.driver)