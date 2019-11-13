import allure
from selenium.webdriver.common.by import By

from appium_po.common.base_page import BasePage
from appium_po.page.market.market_page import MarketPage
from appium_po.page.stock.optional_page import OptionalPage
from appium_po.page.stock.search_page import SearchPage
from appium_po.page.trade.trade_page import TradePage


class XueqiuPage(BasePage):
    _myProfile = (By.ID, 'user_profile_icon')       # 主页中"我的"icon
    _optional_tab = (By.XPATH, '//*[@text="自选"]')
    _xueqiu_tab = (By.XPATH, '//*[@text="雪球"]')
    _trade_tab = (By.XPATH, '//*[@text="交易"]')
    _market_tab = (By.XPATH, '//*[@text="行情"]')
    _ad_skip = (By.ID, "tv_skip")       # 跳过广告
    _ib_close = (By.ID, 'ib_close')     # 关闭弹窗
    _tv_skip = (By.ID, 'tv_skip')       # 引导
    _tv_title = (By.XPATH, '//*[@text="请选择你感兴趣的股票"]')       # 引导页标题
    _iv_close = (By.ID, 'iv_close')     # 下方弹窗关闭按钮
    _update_cancel = (By.ID, 'image_cancel')     # 关闭更新
    _home_search = (By.ID, 'home_search')       # 搜索输入框

    def goto_search(self):
        self.find_and_click(self._home_search)
        return SearchPage(self.driver)

    def goto_profile(self):
        self.find_and_click(self._myProfile)
        from appium_po.page.profile.profile_page import ProfilePage
        return ProfilePage(self.driver)

    def goto_optional(self):
        with allure.step("点击底部导航栏'自选'"):
            ele = self.find(self._optional_tab, min_y_per=0.95)
            ele.click()
        return OptionalPage(self.driver).close_defalut_tip().add_to_portfolio_stock()

    def goto_xueqiu(self):
        with allure.step("点击底部导航栏'雪球'"):
            ele = self.find(self._xueqiu_tab, min_y_per=0.95)
            ele.click()
        return XueqiuPage(self.driver)

    def goto_trade(self):
        with allure.step("点击底部导航栏'交易'"):
            ele = self.find(self._trade_tab, min_y_per=0.95)
            ele.click()
        return TradePage(self.driver)

    def goto_market(self):
        with allure.step("点击底部导航栏'行情'"):
            ele = self.find(self._market_tab, min_y_per=0.95)
            ele.click()
        return MarketPage(self.driver)

    def get_default(self):
        """推荐"""
        return False

    def get_ads(self):
        return False

    def close_update(self):
        with allure.step("关闭更新"):
            skip_btn = self.find(self._update_cancel, timeout=2)
            if skip_btn:
                skip_btn.click()
        return self

    def skip_ads(self):
        with allure.step("处理APP首页广告"):
            skip_btn = self.find(self._ad_skip, timeout=2)
            if skip_btn:
                skip_btn.click()
        return self

    def skip_tv(self):
        with allure.step("处理引导页"):
            skip_btn = self.find(self._tv_skip, timeout=2)
            if skip_btn:
                skip_btn.click()
                if self.find(self._tv_title):
                    self.find_and_click(self._tv_skip)
                self.tap_position(percent=(0.5, 0.5))
                self.find_and_click(self._iv_close)
        return self

    def close_ib(self):
        with allure.step("处理弹窗广告"):
            close_btn = self.find(self._ib_close, timeout=2)
            if close_btn:
                close_btn.click()
        return self


