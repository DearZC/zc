import unittest
import time
from appium import webdriver


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
        # ROLEX['automationName'] = 'Uiautomator2'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', ROLEX)
        time.sleep(3)
        print('打开App')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print('关闭App')

    def test_001_app(self):
        pass


if __name__ == '__main__':
    unittest.main()
