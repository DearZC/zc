
import time

class method():
    def login(self):
        self.driver.find_element_by_id('LoginName').send_keys('lzm')
        time.sleep(2)
        self.driver.find_element_by_id('LoginPwd').send_keys(888888)
        time.sleep(2)
        self.driver.find_element_by_class_name('button_blue').click()

