'''
Created on 2018年9月4日

@author: zc
'''

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def is_toast_exist(driver, toastmessage, timeout = 30, poll_frequency = 0.5):
    ''' is toast exist, return True or False
    - driver: 传driver
    - toastmessage: 页面的toast文本信息
    - timeout: 最大超时时间
    - poll_frequency: 查询间隔时间
    Usage
        is_toast_exist(driver, "toast文本")
    '''
    try :
        toast_loc = ("xpath", ".//*[contains(@text, '%s')]" % toastmessage)
        WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(toast_loc))
        return True
    except :
        return False
    
# def find_toast(driver, toastmessage, timeout, poll_frequency):  #timeout = 30, poll_frequency = 0.01
#     message = '//*[@text = \'{}\']'.format(toastmessage)
#     element = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located((By.XPATH, message))).text
#     print(element)
    
