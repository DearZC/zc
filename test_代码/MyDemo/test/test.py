from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://baijiahao.baidu.com/builder/author/register/index')
driver.find_element_by_xpath("//*[text()='登录']").click()
driver.find_element_by_xpath("//*[text()='用户名登陆']").click()
