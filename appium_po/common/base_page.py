from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

def id(value) -> tuple:
    return MobileBy.ID, value

def accessibility_id(value) -> tuple:
    return MobileBy.ACCESSIBILITY_ID, value

def text(value):
    return MobileBy.XPATH, "//*[@text='%s']" % value

def toast():
    return MobileBy.XPATH, "//*[@class='android.widget.Toast']"


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_toast(self):
        ele = self.driver.find_element(*toast())
        return ele.text if ele else None


    def size(self, locator) -> int:
        return len(self.finds(locator))

    def window_size(self):
        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']
        return x, y

    def find(self, locator, timeout=5, min_x_per=0, min_y_per=0, max_x_per=1, max_y_per=1):
        # 处理弹窗 异常处理 动态浮动元素的处理
        window_x, window_y = self.window_size()
        element = None
        def located_in_correct_position(x):
            try:
                nonlocal element
                element = WebDriverWait(self.driver, timeout/2, 0.5, ignored_exceptions=TimeoutException) \
                    .until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                return False
            else:
                location = element.location
                result_x = min_x_per * window_x <= location['x'] <= max_x_per * window_x
                result_y = min_y_per * window_y <= location['y'] <= max_y_per * window_y
                return result_x and result_y
        try:
            WebDriverWait(self.driver, timeout*2, 0.5, ignored_exceptions=TimeoutException) \
                .until(located_in_correct_position)
            return element
        except TimeoutException:
            return None

    def finds(self, locator, timeout=5):
        try:
            elements = WebDriverWait(self.driver, timeout, 0.5, ignored_exceptions=TimeoutException)\
                .until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            elements = []
        return elements

    def find_invisible(self, locator, timeout=3):
        # 等待元素不存在
        return WebDriverWait(self.driver, timeout, 0.5, ignored_exceptions=TimeoutException) \
                    .until(EC.invisibility_of_element_located(locator))

    def find_and_click(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout, 0.5, ignored_exceptions=TimeoutException)\
            .until(EC.element_to_be_clickable(locator))
        if element: element.click()

    def find_and_sendkeys(self, locator, msg, isclean=True):
        element = self.find(locator)
        if isclean:
            element.clear()
        element.send_keys(msg)

    def find_and_gettext(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout, 0.5, ignored_exceptions=TimeoutException) \
            .until(EC.visibility_of_element_located(locator))
        return element.text if element else None

    def press_search(self):
        self.driver.execute_script("mobile: performEditorAction", {"action": "search"})

    def tap_position(self, position=None, percent=None, duration=None):
        """
        :param position: 手机设备中的坐标位置
        :param percent: 相对于屏幕百分比的位置
        :param duration: 点击时间
        """
        if percent:
            x, y = self.window_size()
            position = [(x*percent[0], y*percent[1])]
        print('position=', position)
        self.driver.tap(positions=position, duration=duration)

    def press_long(self, locator, duration=1500):
        element = WebDriverWait(self.driver, 5, 0.5, ignored_exceptions=TimeoutException)\
            .until(EC.visibility_of_element_located(locator))
        TouchAction(self.driver).long_press(el=element, duration=duration).perform()

    def pageSource(self):
        return self.driver.page_source

