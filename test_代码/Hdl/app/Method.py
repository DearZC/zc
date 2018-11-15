from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

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

        # 元素是否存在
    def is_element_exist(self,element):
        try:
            self.driver.find_element_by_xpath(element)
            print('元素存在')
            return True
        except :
            print('元素不存在')
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

        # 登陆
    def login(self):
        self.driver.find_element_by_android_uiautomator("text(\"请输入手机号码\")").send_keys('18672026447')
        self.driver.find_element_by_android_uiautomator("text(\"请输入密码\")").send_keys('123456')
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id/btnLogin').click()

        # 发布视频动态
    def releaseVideo(self):
        text = '这个是发布的内容'
        self.driver.find_element_by_android_uiautomator("text(\"分享您的那点新鲜事儿...\")").send_keys(text)
        time.sleep(1)
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id/fiv').click()
        # 点击拍照，选择拍视频
        self.driver.find_element_by_android_uiautomator("text(\"拍摄\")").click()
        self.driver.find_element_by_android_uiautomator("text(\"录视频\")").click()
        self.driver.find_element_by_id('com.meizu.media.camera:id/record_start_btn').click()
        time.sleep(15)
        self.driver.find_element_by_id('com.meizu.media.camera:id/btn_done').click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator("text(\"已完成\")").click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator("text(\"发布\")").click()
        time.sleep(1)

        # 发布图片动态
    def releasePhoto(self):
        text = '这个是发布的内容'
        self.driver.find_element_by_android_uiautomator("text(\"分享您的那点新鲜事儿...\")").send_keys(text)
        time.sleep(1)
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id/fiv').click()
        # 点击拍照，选择拍照
        self.driver.find_element_by_android_uiautomator("text(\"拍摄\")").click()
        self.driver.find_element_by_android_uiautomator("text(\"拍照\")").click()
        self.driver.find_element_by_id('com.meizu.media.camera:id/shutter_btn').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.meizu.media.camera:id/btn_done').click()
        self.driver.find_element_by_android_uiautomator("text(\"已完成\")").click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator("text(\"发布\")").click()
        time.sleep(1)

        # 维修预约
    def bespeak(self):
        self.driver.find_element_by_android_uiautomator("text(\"腕表服务中心\")").click()
        # 选择城市--北京
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id/tvLocationCity').click()
        self.driver.find_element_by_android_uiautomator("text(\"确定\")").click()
        # 输入松岗搜索门店并预约
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id/'
                                       'ShopNameSearch').send_keys('西单旗舰')
        self.drvier.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id/llSearch').click()
        self.driver.find_element_by_android_uiautomator("text(\"更多详情\")").click()
        self.driver.find_element_by_android_uiautomator("text(\"立即预约\")").click()
        # 输入预约信息（手表型号，手表问题，姓名，手机，验证码，预约时间）
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id'
                                       '/edWatchModel').send_keys('测试')
        self.driver.find_element_by_android_uiautomator("text(\"零件损坏\")").click()
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id'
                                       '/edRepairMakeAnAppointmentName').send_keys('测试')
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id'
                                       '/edRepairMakeAnAppointmentPhoneNumber').send_keys('18672026447')
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id'
                                       '/edRepairMakeAnAppointmentCode').send_keys('6666')
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id'
                                       '/repairMakeAnAppointmentDate').send_keys('2050-11-11')
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id'
                                       '/repairMakeAnAppointmentTime').send_keys('17:00-18:00')
        self.driver.find_element_by_android_uiautomator("text(\"提交预约\")").click()


















