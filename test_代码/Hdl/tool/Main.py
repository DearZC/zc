from selenium import webdriver
import time
from tkinter import *


# 站群测试
def test():
    word = 'D:/test.xls'
    excel = open(word, 'r', encoding='utf-8')
    lists = []
    for i in excel:
        driver = webdriver.Chrome()
        driver.get(i)
        time.sleep(2)
        title = driver.title
        print(title)
        lists.append(title)
        driver.close()
    excel.close()
    return lists


# 打开新窗口并循环写入数据
def return_listBox():
    run = test()
    top = Toplevel()
    top.title('站群自动化测试结果')
    top.geometry('500x500')
    listBox = StringVar()
    lb = Listbox(top, listvariable=listBox)
    for i in run:
        lb.insert(END, i)
    lb.pack()
