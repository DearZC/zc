import unittest
from selenium import webdriver
import time


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        web = {}
        web['platformName'] = 'Android'
        web['deviceName'] = '79BQADSNPPXDM'
        web['resetKeyboard'] = True
        web['appPackage'] = 'com.android.browser'
        # adb logcat - b events - c   清除ecents日志
        # adb logcat - b events - s am_create_activity:*查看启动日志
        web['appActivity'] = '.BrowserActivity'
        web['noReset'] = True
        web['unicodeKeyboard'] = True  # 默认输入法
        # ROLEX['automationName'] = 'Uiautomator2'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', web)
        time.sleep(3)
        print('打开App')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_001_test(self):
        pass


if __name__ == '__main__':
    unittest.main()
