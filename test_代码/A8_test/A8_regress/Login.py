from appium import webdriver
import unittest
import time
from A8_test.A8_regress.Open import open
from A8_test.A8_regress import Toast


class login(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        A8_Sport = {}
        A8_Sport['platformName'] = 'Android'
        A8_Sport['deviceName'] = '8f08b417'
        A8_Sport['resetKeyboard'] = True    
        A8_Sport['appPackage'] = 'org.fungo.a8sport'
        A8_Sport['appActivity'] = '.ui.activity.MainActivity'
        A8_Sport['noReset'] = True  
        A8_Sport['automationName'] = 'Uiautomator2' 
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', A8_Sport)
        time.sleep(3)
        print('open app')
        
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print('close app')
        time.sleep(3)
    
    def quit(self):
        open.my(self)
        self.driver.swipe(650, 1630, 540, 800, 2000)
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator("text(\"设置\")").click()
        time.sleep(1)
        self.driver.swipe(650, 1630, 540, 800, 2000)
        self.driver.find_element_by_id('org.fungo.a8sport:id/login_text').click()
#        time.sleep(1)
                
    def test_001_wx(self):
        open.my(self)        
        username = self.driver.find_element_by_id('org.fungo.a8sport:id/tvUserName').text

        if username != '点击登录' :
            login.quit(self)
            print('退出登陆')
            self.driver.swipe(540, 800, 650, 1630, 2000)
            time.sleep(1)
            self.driver.find_element_by_id('org.fungo.a8sport:id/ivUserAvatar').click()
            time.sleep(1)
            self.driver.find_element_by_id('org.fungo.a8sport:id/id_imgWechat').click()
            time.sleep(3)
            print('微信登陆')
        else :
            self.driver.find_element_by_id('org.fungo.a8sport:id/ivUserAvatar').click()
            time.sleep(1)
            self.driver.find_element_by_id('org.fungo.a8sport:id/id_imgWechat').click()
            time.sleep(3)
            print('微信登陆')
        self.assertEquals(username, u'点击登录', '没有登陆成功')

    
    def test_002_qq(self):
        open.my(self)   
        username = self.driver.find_element_by_id('org.fungo.a8sport:id/tvUserName').text

        if username != '点击登录' :
            login.quit(self)
            print('退出登陆')
            self.driver.swipe(540, 800, 650, 1630, 2000)
            time.sleep(1)
            self.driver.find_element_by_id('org.fungo.a8sport:id/ivUserAvatar').click()
            time.sleep(1)
            self.driver.find_element_by_id('org.fungo.a8sport:id/qqlogin').click()
            time.sleep(3)
            self.driver.find_element_by_android_uiautomator("text(\"登录\")").click()
            time.sleep(2)
            print('QQ登陆')
        else :
            self.driver.find_element_by_android_uiautomator("text(\"点击登录\")").click()
            time.sleep(1)
            self.driver.find_element_by_id('org.fungo.a8sport:id/qqlogin').click()
            time.sleep(3)
            self.driver.find_element_by_android_uiautomator("text(\"登录\")").click()
            time.sleep(2)
            print('QQ登陆')
        self.assertNotEquals(username, u'点击登录', '没有登陆成功')     
            
    def test_003_wb(self):
        open.my(self)
        username = self.driver.find_element_by_id('org.fungo.a8sport:id/tvUserName').text

        if username != '点击登录' :
            login.quit(self)
            print('退出登陆')
            self.driver.swipe(540, 800, 650, 1630, 2000)
            time.sleep(1)
            self.driver.find_element_by_id('org.fungo.a8sport:id/ivUserAvatar').click()
            time.sleep(1)
            self.driver.find_element_by_id('org.fungo.a8sport:id/weibologin').click()
            time.sleep(3)
            self.driver.find_element_by_android_uiautomator("text(\"确定\")").click()
            time.sleep(2)
            print('微博登陆')
        else :
            self.driver.find_element_by_android_uiautomator("text(\"点击登录\")").click()
            time.sleep(1)
            self.driver.find_element_by_id('org.fungo.a8sport:id/weibologin').click()
            time.sleep(3)
            self.driver.find_element_by_android_uiautomator("text(\"确定\")").click()
            time.sleep(2)
            print('微博登陆')
        self.assertNotEquals(username, u'点击登录', '没有登陆成功')
        
        
    def test_005(self):
        open.my(self)
        login.quit(self)
        a = Toast.is_toast_exist(self.driver, '成功退出当前账号！')
#        Toast.find_toast(self.driver, "成功退出当前账号！", 10, 0.5)
        if a is True:
            print('对的')
        else:
            print('没找到')

if __name__ == '__main__' :
     unittest.main()


