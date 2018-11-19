from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('test')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'c')
js = 'window.open("https://www.baidu.com/");'
driver.execute_script(js)
js = 'window.open("https://www.sogou.com/")'
driver.execute_script(js)
handles = driver.window_handles
driver.switch_to.window(handles[1])
driver.find_element_by_id('query').send_keys(Keys.CONTROL,'v')

