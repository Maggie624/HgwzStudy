from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage
from profile_page import ProfilePage


class ContactPage(BasePage):

    _add_member = (By.XPATH, '//div[@class="ww_operationBar"]//a[text()="添加成员"]')   # 添加成员
    _username = (By.CSS_SELECTOR, '#username')      # 姓名
    _english_name = (By.CSS_SELECTOR, '#memberAdd_english_name')    # 别名
    _id = (By.CSS_SELECTOR, '#memberAdd_acctid')    # 账号
    _phone = (By.CSS_SELECTOR, '#memberAdd_phone')      # 手机
    _save = (By.CSS_SELECTOR, '.js_btn_save')       # 保存
    _tips = (By.CSS_SELECTOR, '#js_tips')       # 保存成功提示
    _memberSearchInput = (By.CSS_SELECTOR, '#memberSearchInput')     # 搜索成员
    _searchResult = (By.CSS_SELECTOR, '#search_member_list li a span:first-child')     # 搜索结果

    def add_member(self, name, alias, id, mobile, **kwargs):
        self.click_and_check(self._add_member, self._username)
        self.sendKeys(*self._username, name)
        self.sendKeys(*self._english_name, alias)
        self.sendKeys(*self._id, id)
        self.sendKeys(*self._phone, mobile)
        self.click_and_check(self._save, self._add_member)
        return self

    def delete_member(self):
        pass

    def get_tips(self):
        tip = self.find_element_by_wait(*self._tips).text
        return tip if tip else ''

    def search(self, key):
        self.sendKeys(*self._memberSearchInput, key)
        def ifsearch(x):
            eles = self.driver.find_elements(*self._searchResult)
            if len(eles) >= 1 and key in eles[0].text:
                return True
        WebDriverWait(self.driver, 4).until(ifsearch)
        return ProfilePage(self.driver)




