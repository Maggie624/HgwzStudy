import allure
import pickle
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from appium_po.page.search_page import SearchPage
from appium_po.page.xueqiu_page import XueqiuPage
import pytest


class TestSearch:

    def setup_class(self):
        self.xueqiu = XueqiuPage()
        self.search = SearchPage(self.xueqiu.driver)

    def teardown_class(self):
        pass


    @pytest.fixture(scope='function')
    def pre_search(self):
        self.xueqiu.goto_search()
        yield
        self.search.cancel_search()

    @pytest.mark.parametrize('key, name, stockCode, price', [
        ('alibaba', '阿里巴巴', 'BABA', 170),
        ('xiaomi', '小米', '01810', 8.0),
        ('google', '谷歌', 'GOOGL', 1000)
    ])
    def test_search(self, key, name, stockCode, price, pre_search):
        self.search.search(key).press_search()
        assert name in self.search.get_name(stockCode)
        assert price < self.search.get_price(stockCode)
