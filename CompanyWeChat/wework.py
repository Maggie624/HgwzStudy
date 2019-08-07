"""
企业微信首页的封装
"""
from selenium import webdriver


class WeWork:

    def __init__(self):
        url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(6)
        self.driver.get(url)
        cookies = {
            'wwrtx.vst': 'xxxxxxx-Biqj1X9FrLJZVK6XrQgBjUopSa-ZjjN2tpUwyxsyrKTEwVsXrxFwCLLy6VqXDtah1t4_dywVD86VM8Lztrcu4gyVOtiMDvLCmGjVX4LlnR7XJxJd_GwwClu2Fk3TNZ-Uzla3yIvpiaw62X34z_bnMaiqlwVPo7obtfkhYmJJEERSXzepyCzoNi0TiM8Mz8A5dSEiIdFmAOFxcpY04fFcB1SFAwwpGh282A',
            'wwrtx.d2st': 'xxxxxxx',
            'wwrtx.sid': 'xxxxxxx-XICNhYdmJ1yL9AIRXXsFC5flyfQBBike',
            'wwrtx.ltype': '1',
            'wxpay.corpid': 'xxxxxxx',
            'wxpay.vid': 'xxxxx',
            'wwrtx.vid': 'xxxxx',
            'wwrtx.logined': 'true'
        }
        for k, v in cookies.items():
            self.driver.add_cookie({'name': k, 'value': v})
        self.driver.get(url)

    def quit(self):
        self.driver.quit()
