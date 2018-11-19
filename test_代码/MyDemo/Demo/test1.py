from bs4 import BeautifulSoup
import requests
from selenium import webdriver


# url = 'http://www.itest.info/courses'
# a = BeautifulSoup(requests.get(url).text, 'html.parser')
# print(a)
#
# for course in  a.find_all('h4'):
#     print(course.text)

# url = 'https://www.v2ex.com/'
# a = BeautifulSoup(requests.get(url).text, 'html.parser')
#
# for i in a.find_all('span', class_ = 'item_hot_topic_title'):
#     # print(i.find('a'))
#     print(i.find('a').text, i.find('a')['href'])


# url = 'https://www.zhihu.com/explore'
# driver = webdriver.Chrome()
# driver.get(url)
#
# element = driver.find_element_by_css_selector('div[data-type="daily"]')
# for i in element.find_elements_by_css_selector('.question_link'):
#     print(i.text)
#
# url = 'https://www.zhihu.com/explore'
# b = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# a = BeautifulSoup(requests.get(url, headers = b).text, 'html.parser')
# print(a.text)
# pageFile = open('D:/pageCode.txt', 'a')
# for j in a.find_all('a', class_ = 'question_link'):
#     print(j.text)
#     pageFile.write(j.text)
# pageFile.close()


from urllib import request
import re
import time
url = 'https://www.zhihu.com/question/22918070'
a = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers = a)
page_info = request.urlopen(page).read()
b = BeautifulSoup(page_info, 'html.parser')
print(b)
print('分割线---------------------')
# pageFile = open('D:/pageCode.txt', 'w', encoding='utf-8')
# pageFile.write(b.text)
# pageFile.close()
soup = b.find_all('img',src = re.compile(r'.jpg$'))
path = 'D:\pic'
x = 0
for img in soup:
    print(img.attrs['src'])
    request.urlretrieve(img.attrs['src'], path + r'\%s.jpg' % x)
    x += 1

# from urllib import request
# url = 'https://www.zhihu.com/explore'
# a = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# page = request.Request(url, headers = a)
# page_info = request.urlopen(page).read()
# b = BeautifulSoup(page_info, 'html.parser')
# print(b.text)
# pageFile = open('D:/pageCode.txt', 'a')
# for j in b.find_all('a', class_ = 'question_link'):
#     print(j.text)
#     pageFile.write(j.text)
# pageFile.close()




