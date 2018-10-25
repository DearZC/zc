from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(2)
    # 截取当前界面并保存到相应位置
# driver.get_screenshot_as_file('D:/zi.jpg')

def isElementExist(element):
    try :
        driver.find_elements_by_css_selector(element)
        print('元素已找到')
        return True
    except :
        print('未找到元素')
        return False
print(isElementExist('#kw'))
time.sleep(2)
driver.quit()




