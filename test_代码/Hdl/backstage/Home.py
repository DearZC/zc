import unittest
import time
from selenium import webdriver
from Hdl.backstage import Method

class home(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.acloudwebs.com/Login/')
        print('打开网址')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print('关闭浏览器')
        time.sleep(2)

    def test_001_login(self):
        Method.method.login(self)
        time.sleep(2)
        self.driver.get_screenshot_as_file('D://test_001_login.png')
        text = self.driver.find_element_by_xpath("//a[@id = 'mb2']/span/span/span").text
        self.assertEqual(text, u'用户注销', '登陆失败')
        time.sleep(3)

    def test_002_DataRreport(self):
        self.driver.find_element_by_id('_easyui_tree_2').click()
        time.sleep(2)
        self.driver.find_element_by_id('_easyui_tree_18').click()
        self.driver.get_screenshot_as_file('D://test_002_DataRreport.png')
        text = self.driver.find_element_by_xpath("//*[text()='数据报表']").text
        self.assertEqual(text, u'数据报表', '未打开数据报表')

    def test_003_quit(self):
        self.driver.find_element_by_xpath("//*[text()='退出']").click()
        self.driver.get_screenshot_as_file('D://test_003_quit.png')
        text = self.driver.find_element_by_id('switch_qlogin').text
        self.assertEqual(text, u'快速登录', '退出失败')

if __name__ == '__main__':
    unittest.main()

