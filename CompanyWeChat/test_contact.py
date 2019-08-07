import os,sys

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from contact_page import ContactPage
from profile_page import ProfilePage
from manage_page import ManagePage
from wework import WeWork
import time


class TestContact:
    def setup_class(self):
        self.base = WeWork()
        self.contact = ContactPage(self.base.driver)
        self.profile = ProfilePage(self.base.driver)
        self.manage = ManagePage(self.base.driver)

    def teardown_class(self):
        time.sleep(5)
        self.base.quit()

    def test_add_member_英文(self):
        self.contact.add_member('Ariel', 'ariel', '006', '18800000003')
        assert self.contact.get_tips() == '保存成功'
        def tips(x):
            return self.contact.get_tips() == ""
        WebDriverWait(self.contact.driver, 5).until(tips)

    def test_add_member_中文(self):
        self.contact.add_member('张三', '张三', '008', '18800000005')
        assert self.contact.get_tips() == '保存成功'
        def tips(x):
            return self.contact.get_tips() == ""
        WebDriverWait(self.contact.driver, 6).until(tips)

    def test_delete(self):
        # udid = str(time)
        # self.contact.add_member('Ariel'+udid, 'ariel'+udid, '006'+udid, '18800000003')
        # self.contact.delete_member()
        pass

    def test_update_profile(self):
        self.contact.search('张三')
        self.profile.update('彼得', 'Peter', '18800000008')
        assert self.contact.get_tips() == '保存成功'
        def tips(x):
            return self.contact.get_tips() == ""
        WebDriverWait(self.contact.driver, 6).until(tips)

    def test_disable_profile(self):
        self.contact.search('Ariel')
        self.profile.disable()
        assert self.contact.get_tips() == '禁用成功'
        def tips(x):
            return self.contact.get_tips() == ""
        WebDriverWait(self.contact.driver, 6).until(tips)

    def test_enable_profile(self):
        self.contact.search('Ariel')
        self.profile.enable()
        assert self.contact.get_tips() == '启用成功'
        def tips(x):
            return self.contact.get_tips() == ""
        WebDriverWait(self.contact.driver, 6).until(tips)

    def test_add_pic(self):
        self.manage.open_managetools()
        self.manage.goto_material()
        self.manage.add_pic()



