
import unittest
from appium import webdriver
import time
from A8_regress.Open import open


class version(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        A8_Sport = {}
        A8_Sport['platformName'] = 'Android'
        A8_Sport['deviceName'] = '8f08b417'
        A8_Sport['resetKeyboard'] = True    
        A8_Sport['appPackage'] = 'org.fungo.a8sport'
        A8_Sport['appActivity'] = '.ui.activity.MainActivity'
        A8_Sport['noReset'] = True  
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', A8_Sport)
        time.sleep(3)
        print('open app')
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print('close app')
        time.sleep(3)
        
    def test_001_version(self):
        open.my(self)
        self.driver.swipe(650, 1630, 540, 800, 2000)
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator("text(\"设置\")").click()
        time.sleep(1)
        version = self.driver.find_element_by_id('org.fungo.a8sport:id/setting_version_name').text
        self.assertEqual(version, u'4.6.0_dev_300403', '版本号不正确')


if __name__ == '__main__' :
    unittest.main()
            