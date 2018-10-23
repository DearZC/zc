import unittest
import time
from selenium import webdriver
from Hdl.xiHeng.Method import findElement


class home(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bj.watch-vip.cn/")
        print("打开网址")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("关闭浏览器")
    
    def test_001_maintenance(self):
        time.sleep(5)
        self.driver.find_element_by_class_name("reservation-shadow-close").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[text()='微信联系']").click()
        self.driver.get_screenshot_as_file('E:/XiHeng/test_001_maintenance.png')
        element = '.sidebar-cell-popup.sidebar-cell-popup-qr'
        a = findElement.isElementExist(self,element)
        self.assertTrue(a, '正确')

if __name__ == '__main__' :
    unittest.main()