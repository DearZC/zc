
class findElement :
    # 元素是否存在
    def isElementExist(self, element):
        try :
            self.driver.find_elements_by_css_selector(element)
            print('元素已找到')
            return True
        except :
            print('未找到元素')
            return False



