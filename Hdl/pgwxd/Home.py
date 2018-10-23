
import unittest
import time
from selenium import webdriver

class home(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.pgwxd.com/")
        print("打开首页")
        
    def tearDown(self):
        self.driver.quit()
        print("关闭浏览器")
    
    def test_001_maintenance(self):
        time.sleep(5)
        self.driver.find_element_by_class_name("mip-selected-region").click()
        time.sleep(5)
        
        
if __name__ == '__main__' :
    unittest.main()