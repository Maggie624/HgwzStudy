import os
import sys

import pytest


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from appium_po.page.market.market_fund_page import MarketFundPage
from appium_po.page.market.market_page import MarketPage
from appium_po.driver.xueqiu import XueqiuDriver
from appium_po.page.main.xueqiu_page import XueqiuPage


class TestMerketFund:
    def setup_class(self):
        self.driver = XueqiuDriver()
        self.xueqiu = XueqiuPage(self.driver)
        self.market = MarketPage(self.driver)
        self.market_fund = MarketFundPage(self.driver)

    @pytest.fixture(scope='function')
    def clean(self):
        yield
        self.xueqiu.goto_xueqiu()

    def test_fund(self, clean):
        self.xueqiu.goto_market().goto_fund().goto_index_rank()
        increase_ranges = self.market_fund.all_increase_range()
        print(increase_ranges, end='11111\n')
        list_positive = sorted([item for item in increase_ranges if not item.startswith('-')], reverse=True)
        list_negative = sorted([item for item in increase_ranges if item.startswith('-')], reverse=False)
        sorted_list = list_positive + list_negative
        print(sorted_list, end='22222\n')
        assert increase_ranges == sorted_list
