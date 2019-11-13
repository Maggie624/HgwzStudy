import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from appium_po.page.stock.search_page import SearchPage
from appium_po.page.main.xueqiu_page import XueqiuPage
import pytest
from appium_po.driver.xueqiu import XueqiuDriver


class TestSearch:
    def setup_class(self):
        self.driver = XueqiuDriver()
        self.xueqiu = XueqiuPage(self.driver)
        self.search = SearchPage(self.driver)


    @pytest.fixture(scope='function')
    def pre_search(self):
        self.xueqiu.goto_search()
        yield
        self.search.cancel_search()

    @pytest.mark.parametrize('key, name, stockCode, price', [
        ('alibaba', '阿里巴巴', 'BABA', 160),
        ('xiaomi', '小米', '01810', 8.0),
        ('google', '谷歌', 'GOOGL', 1000)
    ])
    def test_search(self, key, name, stockCode, price, pre_search):
        self.search.search(key).press_search()
        assert name in self.search.get_name(stockCode)
        assert price < self.search.get_price(stockCode)
