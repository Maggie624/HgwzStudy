from selenium.webdriver.support.wait import WebDriverWait

from appium_po.common.base_page import BasePage, id, text
from appium_po.page.main.xueqiu_page import XueqiuPage


class ProfilePage(BasePage):
    _login_more = id('login_more')      # 更多方式登录
    _action_back = id('action_back')       # 返回上一层
    _phone = id('rl_login_phone')       # 手机登录
    _wechat = id('iv_login_wx')
    _weibo = id('rl_login_weibo')
    _qq = id('rl_login_qq')
    _phone_input = id('register_phone_number')      # 手机号
    _phone_captch = id('register_code')     # 验证码
    _phone_next = id('button_next')
    _phone_msg = id('md_content')
    _close_msg = text('确定')
    _iv_action_back = id('iv_action_back')     # 取消登录



    def goto_login_more(self):
        self.find_and_click(self._login_more)
        from appium_po.page.profile.login_page import LoginPage
        return LoginPage(self.driver)

    def goto_xueqiu(self):
        self.find_and_click(self._action_back)
        return XueqiuPage(self.driver)


    def login_by_phone(self, phone, captch):
        self.find_and_click(self._phone)
        self.find_and_sendkeys(self._phone_input, phone)
        self.find_and_sendkeys(self._phone_captch, captch)
        def find_msg(x):
            self.find_and_click(self._phone_next, timeout=2)
            ele = self.find(self._phone_msg, timeout=2)
            if ele is not None:
                return True
        WebDriverWait(self.driver, 10).until(find_msg)
        return self

    def login_by_wechat(self):
        self.find_and_click(self._wechat)
        return self

    def login_by_weibo(self):
        pass

    def login_by_qq(self):
        pass

    def is_msg_exist(self, msg):
        print(self.size(self.finds(text(msg))) >= 1)
        return self.size(self.finds(text(msg))) >= 1

    def goto_profile(self):
        """从手机号登录页面返回到登录方式选择页"""
        self.find_and_click(self._iv_action_back)
        # self.find_and_click(self._leave)
        return ProfilePage(self.driver)

    def close_msg(self):
        self.find_and_click(self._close_msg)
        return self
