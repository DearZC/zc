import unittest
from selenium import webdriver
import time


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        driver = webdriver.Chrome()
        driver.get('http://vip.cdmbwx.com')
        time.sleep(1)

    def test_001_test(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
