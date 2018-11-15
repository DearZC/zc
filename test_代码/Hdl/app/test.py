from appium import webdriver
import time


ROLEX = {}
ROLEX['platformName'] = 'Android'
ROLEX['deviceName'] = '79BQADSNPPXDM'
ROLEX['resetKeyboard'] = True
ROLEX['appPackage'] = 'com.hengdeliltd.wristwatch.household.activity'
        # adb logcat - b events - c   清除ecents日志
        # adb logcat - b events - s am_create_activity: *查看启动日志
ROLEX['appActivity'] = '.LauncherActivity'
ROLEX['noReset'] = True
ROLEX['unicodeKeyboard'] = True   #  默认输入法
ROLEX['automationName'] = 'Uiautomator2'
driver = webdriver.Remote('http://localhost:4723/wd/hub', ROLEX)
time.sleep(3)
print('打开App')


def is_element_exist(element):
    try:
        driver.find_element_by_xpath(element)
        print('元素存在')
        return True
    except:
        print('元素不存在')
        return False

driver.find_element_by_android_uiautomator("text(\"我的\")").click()
element = '//android.widget.ImageView'
a = is_element_exist(element)
print(a)



