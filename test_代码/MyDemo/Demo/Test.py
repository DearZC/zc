from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#driver.save_screenshot('D:/test.png')
nowTime = time.strftime('%Y%m%d.%H.%M.%S')
t = driver.get_screenshot_as_file('D:/%s.png' %('test_001'+ '('+ nowTime+ ')'))
print('截图为：%s'%t)
print(t)
driver.quit()