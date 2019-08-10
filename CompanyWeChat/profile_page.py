from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage
import time


class ProfilePage(BasePage):
    _edit = (By.CSS_SELECTOR, '.js_edit')       # 编辑
    _alias = (By.NAME, 'english_name')       # 别名
    _name = (By.NAME, 'username')      # 姓名
    _phone = (By.NAME, 'mobile')        # 手机
    _disable = (By.XPATH, '//a[text()="禁用"]')       # 禁用
    _enable = (By.XPATH, '//a[text()="启用"]')       # 启用
    _submit = (By.XPATH, '//a[@d_ck="submit"]')     # 确认
    _save = (By.CSS_SELECTOR, '.js_save')       # 保存

    def update(self, name, alias, mobile):
        self.click_by_sele(*self._edit)
        self.sendKeys(*self._name, name)
        self.sendKeys(*self._alias, alias)
        self.sendKeys(*self._phone, mobile)
        self.click_and_check(self._save, self._edit)

    def disable(self):
        self.click_by_sele(*self._disable)
        self.click_and_check(self._submit, self._enable)

    def enable(self):
        self.click_and_check(self._enable, self._disable)

    def delete(self):
        pass
