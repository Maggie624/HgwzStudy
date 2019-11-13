import allure

from appium_po.common.base_page import BasePage, id, text

class MarketFundPage(BasePage):
    _index_rank = text('指数排行')
    _increase_range = id('column_three')

    def goto_index_rank(self):
        with allure.step('点击指数排行'):
            self.find_and_click(self._index_rank)

    def all_increase_range(self):
        with allure.step('获取当前页面所有日涨幅信息'):
            eles = self.finds(self._increase_range)
        text_list = [ele.text.replace('+', '') for ele in eles]
        return text_list
