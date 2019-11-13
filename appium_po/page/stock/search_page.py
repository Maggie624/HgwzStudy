from selenium.webdriver.common.by import By

from appium_po.common.base_page import BasePage


class SearchPage(BasePage):

    _canel = (By.ID, 'action_close')        # 取消搜索
    _search_text = (By.ID, 'search_input_text')     # 搜索内容文本
    _follow_stock = (By.XPATH,
                           "//*[@text='{name}']/../..//*[contains(@resource-id, 'add_attention')]//*[contains(@resource-id,'follow_btn')]")     # 未添加的股票按钮
    _followed_stock = (By.XPATH,
                           "//*[@text='{name}']/../..//*[contains(@resource-id, 'add_attention')]//*[contains(@resource-id,'followed_btn')]")       # 已添加的股票按钮
    _next_comment = (By.ID, 'md_buttonDefaultNegative')     # 下次再说


    def search(self, keyword):
        self.find_and_sendkeys(self._search_text, keyword)
        # self.driver.execute_script("mobile: performEditorAction", {"action": "search"})
        return self

    def select(self, index):
        self.driver.find_elements_by_id('name')[index].click()
        return self

    def get_price(self, stock_code):
        # price = self.driver.find_element_by_xpath("//*[contains(@resource-id, stockCode) and @text='"+stock_code+"']"
        #                                           "/../../..//*[contains(@resource-id,'current_price')]").text
        price = self.find_and_gettext((By.XPATH, "//*[contains(@resource-id, stockCode) and @text='"+stock_code+"']"
                                                        "/../../..//*[contains(@resource-id,'current_price')]"))
        return float(price) if price else None

    def get_name(self, stock_code):
        # name = self.driver.find_element_by_xpath("//*[contains(@resource-id, 'stockCode') and @text='"+stock_code+"']"
        #                                          "/../..//*[contains(@resource-id, 'stockName')]").text
        name = self.find_and_gettext((By.XPATH, "//*[contains(@resource-id, 'stockCode') and @text='"+stock_code+"']"
                                                       "/../..//*[contains(@resource-id, 'stockName')]"))
        return name

    def cancel_search(self):
        self.find_and_click(self._canel)
        return self

    def add_searched_stock(self, stockName):
        self.find_and_click((self._follow_stock[0], self._follow_stock[1].format(name=stockName)))
        tip = self.find(self._next_comment)
        if tip:
            tip.click()

    def searched_stock_status(self, stockName, isfollowed=True):
        if isfollowed:
            ele = self.find((self._followed_stock[0], self._followed_stock[1].format(name=stockName)))
        else:
            ele = self.find((self._follow_stock[0], self._follow_stock[1].format(name=stockName)))
        if ele:
            return ele.text
        else:
            return None

