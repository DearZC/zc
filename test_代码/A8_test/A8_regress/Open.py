# coding=utf-8


import time
 
 
class open():
         
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
        
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['heigth']
        return(x, y)