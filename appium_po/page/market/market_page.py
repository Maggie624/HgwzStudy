import allure

from appium_po.common.base_page import BasePage, id
from ..market.market_fund_page import MarketFundPage

class MarketPage(BasePage):
    _stock = id('page_type_stock')
    _fund = id('page_type_fund')

    def goto_stock(self):
        with allure.step("点击行情-股票tab"):
            self.find_and_click(self._stock)
        return self

    def goto_fund(self):
        with allure.step("点击行情-基金tab"):
            self.find_and_click(self._fund)
        return MarketFundPage(self.driver)

