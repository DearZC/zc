from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('test')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'c')
js = 'window.open("https://www.baidu.com/");'
driver.execute_script(js)
handles = driver.window_handles
driver.switch_to_window(handles[1])
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
