from selenium import webdriver
import time
import unittest

class StationGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.baidu.com')
        print('打开浏览器网页\n')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('关闭浏览器')

    def test_001_test(self):
        str = input('请输入搜索内容：')
        self.driver.find_element_by_id('kw').send_keys(str)
        self.driver.find_element_by_id('su').click()

        self.driver.back()

        self.driver.find_element_by_id('kw').send_keys('456789')

        print(self.driver.title)
        print(self.driver.current_url)
        print(self.driver.capabilities['version'])


if __name__ == '__main__':
    unittest.main()


