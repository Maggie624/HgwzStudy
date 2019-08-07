from selenium.webdriver.common.by import By

from base_page import BasePage
import time

class ManagePage(BasePage):

    _material = (By.XPATH, '//a[@href="#material/text"]/..')        # 素材库
    _mpnews = (By.XPATH, '//a[@href="#material/image"]/..')        # 图文
    _create = (By.XPATH, '//*[contains(text(),"添加图片")]')       # 添加图片btn
    _uploadImageFile = (By.CSS_SELECTOR, '#js_upload_input')     # 上传图片，加号
    _uploadcancel = (By.CSS_SELECTOR, '.js_uploadProgress_cancel')      # 取消上传
    _submit = (By.XPATH, '//*[@d_ck="submit"]')     # 完成


    def open_managetools(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#manageTools')

    def goto_material(self):
        self.click_by_sele(*self._material)

    def add_pic(self):
        self.click_by_sele(*self._mpnews)
        self.click_by_sele(*self._create)       # 添加图片
        self.sendKeys(*self._uploadImageFile, '/Users/maoqi/Desktop/zyx.jpg')
        self.find_element_invisibility(*self._uploadcancel)
        self.click_by_sele(*self._submit)



