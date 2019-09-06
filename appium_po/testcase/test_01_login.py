import pytest
import os, sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from appium_po.page.login_page import LoginPage
from appium_po.page.profile_page import ProfilePage
from appium_po.page.xueqiu_page import XueqiuPage
from appium_po.driver.xueqiu import XueqiuDriver

class TestLogin:

    def setup_class(self):
        self.driver = XueqiuDriver()
        self.xueqiu = XueqiuPage(self.driver)
        self.profile = ProfilePage(self.driver)
        self.login = LoginPage(self.driver)

    def teardown_class(self):
        self.login.goto_profile()
        self.profile.goto_xueqiu()
        # self.driver.close_app()

    @pytest.fixture(scope='function')
    def close_msg(self):
        yield
        self.login.close_msg()

    def test_login_01_wrong_phone(self, close_msg):
        self.xueqiu.goto_profile()
        self.profile.goto_login_more()
        self.login.login('1234567890', '888888')
        assert self.login.login_msg() == '手机号码填写错误'

    def test_login_02_wrong_psw(self, close_msg):
        self.login.login('18312121111', '888888')
        assert self.login.login_msg() == '用户名或密码错误'