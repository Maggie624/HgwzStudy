import allure
from selenium.webdriver.common.by import By

from appium_po.common.base_page import BasePage
from appium_po.page.stock.search_page import SearchPage


class OptionalPage(BasePage):
    """自选"""
    _tip = (By.ID, 'snb_tip_text')      # 新增手势切换、指标设置功能
    _search = (By.ID, "action_search")      # 搜索按钮
    _stock = (By.XPATH, "//*[@text='平安银行']/../..")
    _operation = (By.ID, 'md_title')        # 对股票进行更多操作
    _deleteStock = (By.XPATH, '//*[@text="删除"]')
    _stockName = (By.ID, "portfolio_stockName")
    _add_to_portfolio_stock = (By.ID, 'add_to_portfolio_stock')     # 加入自选股

    def add_to_portfolio_stock(self):
        ele = self.find(self._add_to_portfolio_stock)
        if ele:
            ele.click()
        return self

    def close_defalut_tip(self):
        ele = self.find(self._tip)
        if ele:
            x, y = self.window_size()
            self.tap_position([(x*0.5, y*0.5)])
        return self

    def goto_search(self):
        ele = self.find(self._search, max_y_per=0.15)
        ele.click()
        return SearchPage(self.driver)

    def delete_stock(self, stockName):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().text("'+stockName+'").instance(0));')
        with allure.step("长按股票信息"):
            self.press_long(self._stock, duration=2000)
        with allure.step("点击删除股票"):
            self.find_and_click(self._deleteStock)

    def all_stockName_in_selected_list(self):
        elements = self.finds(self._stockName)
        names = []
        for item in elements:
            names.append(item.text)
        return names

