# coding=utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("setf").click()
js = 'window.open("http://www.sogou.com/");'
driver.execute_script(js)
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[0])
print(driver.current_window_handle)
driver.switch_to.window(handles[1])
print(driver.current_window_handle)
driver.switch_to.window(handles[2])
print(driver.current_window_handle)
