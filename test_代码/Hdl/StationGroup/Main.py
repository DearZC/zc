from selenium import webdriver
import time

if __name__ == '__main__' :
    # b = [1,1,2,3,5,2,3,4,5,6,6,3]
    # b = list(set(b))
    # print(b)
    word = 'D:/test.xls'
    a = open(word, 'r', encoding='utf-8')
    for i in a:
        print (i)
        driver = webdriver.Chrome()
        driver.get(i)
        driver.close()
    a.close()