import os
import sys

import allure
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from appium_po.page.main.xueqiu_page import XueqiuPage
from appium_po.page.stock.optional_page import OptionalPage
from appium_po.page.stock.search_page import SearchPage
from appium_po.driver.xueqiu import XueqiuDriver

class TestAddStock:

    def setup_class(self):
        self.driver = XueqiuDriver()
        self.xueqiu = XueqiuPage(self.driver)
        self.optional = OptionalPage(self.driver)
        self.search = SearchPage(self.driver)

    def teardown_class(self):
        self.xueqiu.goto_xueqiu()

    @pytest.fixture(scope="function")
    def pre_01(self):
        self.xueqiu.goto_optional().goto_search()
        yield
        self.search.cancel_search()

    @pytest.fixture(scope="function")
    def pre_02(self):
        self.optional.goto_search()
        yield
        self.search.cancel_search()

    @allure.story("添加股票")
    def test_01_add_stock(self, pre_01):
        self.search.search('pingan').press_search()
        self.search.add_searched_stock('平安银行')
        assert '已添加' == self.search.searched_stock_status('平安银行')

    @allure.story("搜索已添加的股票，显示为'已添加'")
    def test_02_search_again(self, pre_02):
        self.search.search('pingan').press_search()
        assert '已添加' == self.search.searched_stock_status('平安银行')

    @allure.story("删除股票")
    def test_03_delete_stock(self):
        self.optional.delete_stock("平安银行")
        assert '平安银行' not in self.optional.all_stockName_in_selected_list()
