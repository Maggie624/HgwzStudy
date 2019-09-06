from selenium.webdriver.common.by import By

from appium_po.page.base_page import BasePage
from appium_po.page.xueqiu_page import XueqiuPage


class ProfilePage(BasePage):
    _login_more = (By.ID, 'login_more')      # 更多方式登录
    _action_back = (By.ID, 'action_back')       # 返回上一层


    def goto_login_more(self):
        self.find_and_click(self._login_more)
        from appium_po.page.login_page import LoginPage
        return LoginPage(self.driver)

    def goto_xueqiu(self):
        self.find_and_click(self._action_back)
        return XueqiuPage(self.driver)


