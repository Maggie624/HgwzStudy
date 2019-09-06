from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

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
        elements = WebDriverWait(self.driver, timeout, 0.5, ignored_exceptions=TimeoutException)\
            .until(EC.visibility_of_all_elements_located(locator))
        return elements

    def find_and_click(self, locator):
        element = WebDriverWait(self.driver, 5, 0.5, ignored_exceptions=TimeoutException)\
            .until(EC.element_to_be_clickable(locator))
        element.click()

    def find_and_sendkeys(self, locator, msg, isclean=True):
        element = self.find(locator)
        if isclean:
            element.clear()
        element.send_keys(msg)

    def press_search(self):
        self.driver.execute_script("mobile: performEditorAction", {"action": "search"})

    def tap_position(self, position=None, percent=None, duration=None):
        if percent:
            x, y = self.window_size()
            position = [(x*percent[0], y*percent[1])]
        print('position=', position)
        self.driver.tap(positions=position, duration=duration)

    def press_long(self, locator, duration=1500):
        element = WebDriverWait(self.driver, 5, 0.5, ignored_exceptions=TimeoutException)\
            .until(EC.visibility_of_element_located(locator))
        TouchAction(self.driver).long_press(el=element, duration=duration).perform()

