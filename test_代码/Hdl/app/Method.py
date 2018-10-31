from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class toast():

    def is_toast_exist(driver, toastmessage, timeout = 30, poll_frequency = 0.5):
        ''' is toast exist, return True or False
    - driver: 传driver
    - toastmessage: 页面的toast文本信息
    - timeout: 最大超时时间
    - poll_frequency: 查询间隔时间
    Usage
        is_toast_exist(driver, "toast文本")
    '''
        try :
            toast_loc = ("xpath", ".//*[contains(@text, '%s')]" % toastmessage)
            WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
            return True
        except :
            return False

        # 获取屏幕大小
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

        # 向上滑动
    def swipUp(self, t):
        size = self.get_size()
        self.driver.swip(size[0]*0.5, size[1]*0.75, size[0]*0.5, size[1]*0.25, t)

        # 向下滑动
    def swipDown(self, t):
        size = self.get_size()
        self.driver.swip(size[0]*0.5, size[1]*0.25, size[0]*0.5, size[1]*0.75, t)

        # 向左滑动
    def swipLeft(self, t):
        size = self.get_size()
        self.driver.swip(size[0]*0.75. size[1]*0.5, size[0]*0.25, size[1]*0.5, t)

        # 向右滑动
    def swipRight(self, t):
        size = self.get_size()
        self.driver.swip(size[0] * 0.25.size[1] * 0.5, size[0] * 0.75, size[1] * 0.5, t)

        # 点击首页
    def home(self):
        self.driver.find_element_by_xpath("//*[text()='首页']").click()

        # 点击社区
    def community(self):
        self.driver.find_element_by_xpath("//*[text()='社区']").click()

        # 点击我的
    def my(self):
        self.driver.find_element_by_xpath("//*[text()='我的']").click()

