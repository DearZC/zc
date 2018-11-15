import unittest
import time
from appium import webdriver
from app.Method import toast


class home(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        ROLEX = {}
        ROLEX['platformName'] = 'Android'
        ROLEX['deviceName'] = '79BQADSNPPXDM'
        ROLEX['resetKeyboard'] = True
        ROLEX['appPackage'] = 'com.hengdeliltd.wristwatch.household.activity'
        # adb logcat - b events - c   清除ecents日志
        # adb logcat - b events - s am_create_activity: *查看启动日志
        ROLEX['appActivity'] = '.LauncherActivity'
        ROLEX['noReset'] = True
        ROLEX['unicodeKeyboard'] = True   #  默认输入法
        ROLEX['automationName'] = 'Uiautomator2'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', ROLEX)
        time.sleep(3)
        print('打开App')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print('关闭App')

    def test_001_login(self):
        self.driver.find_element_by_android_uiautomator("text(\"我的\")").click()
        time.sleep(2)
        element = "//*[@resource-id = 'com.hengdeliltd.wristwatch.household.activity:id/btnLogin']"
        i = toast.is_element_exist(self,element)
        print(i)
        if i is True:
            print('找到元素，当前未登陆，进行登陆')
            toast.login(self)
        else:
            print('没有找到元素，当前已登陆，不执行操作')
            pass
        time.sleep(2)

    def test_002_releaseVideo(self):
        self.driver.find_element_by_android_uiautomator("text(\"社区\")").click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id/ivReleasePhotograph').click()
        toast.releaseVideo(self)
        a = toast.is_toast_exist(self.driver, '发布成功')
        if a is True:
            print('发布成功')
        else:
            print('发布失败')

    def test_003_releasePhoto(self):
        self.driver.find_element_by_android_uiautomator("text(\"社区\")").click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id/ivReleasePhotograph').click()
        toast.releasePhoto(self)
        a = toast.is_toast_exist(self.driver, '发布成功')
        if a is True:
            print('发布成功')
        else:
            print('发布失败')

    def test_004_order(self):
        self.driver.find_element_by_android_uiautomator("text(\"我的\")").click()
        self.driver.find_element_by_id('com.hengdeliltd.wristwatch.household.activity:id/lltvPersonal').click()
        toast.bespeak(self)
        a = self.driver.find_element_by_android_uiautomator("text(\"尊敬的用户，恭喜您已预约成功\")").text()
        # self.assertEqual(a, '尊敬的用户，恭喜您已预约成功', 'message = 没有预约成功')
        print(a)



if __name__ == '__main__':
    unittest.main()
