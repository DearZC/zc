import unittest
import time
from appium import webdriver


class home(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        A8_Sport = {}
        A8_Sport['platformName'] = 'Android'
        A8_Sport['deviceName'] = ''
        A8_Sport['resetKeyboard'] = True
        A8_Sport['appPackage'] = ''
        A8_Sport['appActivity'] = ''
        A8_Sport['noReset'] = True
        A8_Sport['unicodeKeyboard'] = True   #  默认输入法
        A8_Sport['automationName'] = 'Uiautomator2'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', A8_Sport)
        time.sleep(3)
        print('打开App')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print('关闭App')


if __name__ == '__main__':
    unittest.main()
