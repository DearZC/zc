# coding=utf-8


import time
 
 
class open():
    
#     @classmethod
#     def setUpClass(self):
#         A8_Sport = {}
#         A8_Sport['platformName'] = 'Android'
#         A8_Sport['deviceName'] = '8f08b417'
# #        A8_Sport['unicodeKeyboard'] = True  # 设置appium默认输入法
#         A8_Sport['resetKeyboard'] = True    
#         A8_Sport['appPackage'] = 'org.fungo.a8sport'
#         A8_Sport['appActivity'] = '.ui.activity.MainActivity'
#         A8_Sport['noReset'] = True  
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', A8_Sport)
#         time.sleep(3)
#         print('open app')
         
    def my(self):        
        self.driver.find_element_by_xpath('//android.widget.TextView[@text = \'我的\']').click()
        time.sleep(3)
        print('我的界面')
       
    def community(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text = \'社区\']').click()
        time.sleep(3)
        print('社区界面')
       
    def match(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text = \'比赛\']').click()
        time.sleep(3)
        print('比赛界面')
     
