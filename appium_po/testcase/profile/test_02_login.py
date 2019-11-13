import pytest
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from appium_po.driver.xueqiu import XueqiuDriver
from appium_po.page.main.xueqiu_page import XueqiuPage
from appium_po.page.profile.profile_page import ProfilePage


class TestLoginPage:

    def setup_class(self):
        self.driver = XueqiuDriver()
        self.xueqiu = XueqiuPage(self.driver)
        self.profile = ProfilePage(self.driver)

    @pytest.fixture(scope='function')
    def setting_for_login_by_phone(self):
        yield
        self.profile.close_msg()
        self.profile.goto_profile()

    def test_login_by_phone(self, setting_for_login_by_phone):
        self.xueqiu.goto_profile().login_by_phone('18312121212', '1212')
        assert '验证码已过期' in self.profile.pageSource()

    def test_login_by_wechat(self):
        self.profile.login_by_wechat()
        assert '您尚未安装微信，请先安装微信' in self.profile.get_toast()

    # def test_login_by_weibo(self):
    #     self.fail()
    #
    # def test_login_by_qq(self):
    #     self.fail()


    # def test_notification(self):
    #     '''﻿读取短信'''
    #     self.driver.open_notifications()
    #     time.sleep(3)
    #     print(self.driver.page_source)
    #     print(self.xueqiu.find_and_gettext((By.ID, 'android:id/message_text')), end='niubi!!!!\n')
    #     self.xueqiu.tap_position(percent=(0.5, 0.95))
