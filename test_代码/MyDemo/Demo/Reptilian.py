import urllib.request
from urllib import request
from bs4 import BeautifulSoup

# url = 'http://www.baidu.com'
# page_info = urllib.request.urlopen(url).read()
# page_info = page_info.decode('utf-8')
# print(page_info)


# url = 'http://www.baidu.com'
# a = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# page = request.Request(url, headers = a)
# page_info = request.urlopen(page).read().decode('utf-8')
# print(page_info)

# url = 'http://www.baidu.com'
# a = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# page = request.Request(url, headers = a)
# page_info = request.urlopen(page).read().decode('utf-8')
# soup = BeautifulSoup(page_info, 'html.parser')
# titles = soup.find_all('a', 'title')
# try :
#     text = 'D://pachong.txt'
#     file = open(text, 'w')
#     for title in titles :
#         file.write(title.string + '/n')
# finally:
#     if file :
#         file.close()


# from urllib import request
# from bs4 import BeautifulSoup
# url = r'http://www.jianshu.com'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
# page = request.Request(url, headers=headers)
# page_info = request.urlopen(page).read().decode('utf-8')
# soup = BeautifulSoup(page_info, 'html.parser')
# titles = soup.find_all('a', 'title')
# try:
# # 在E盘以只写的方式打开/创建一个名为 titles 的txt文件
#     file = open(r'D:\titles.txt', 'w')
#     for title in titles: # 将爬去到的文章题目写入txt中
#         file.write(title.string + '/n')
# finally:
#     if file: # 关闭文件（很重要）
#         file.close()

# with open('D:\titles.txt', 'w') as fail :
#     for title in titles :
#         file.write(title.string + '\n')

from urllib import request
from bs4 import BeautifulSoup
import time
import re

url = 'https://www.zhihu.com/question/22918070'
a = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers = a)
page_info = request.urlopen(page).read().decode('utf-8')
soup = BeautifulSoup(page_info, 'html.parser')

links = soup.find_all('img', 'origin_image zh-lightbox-thumb', src=re.compile(r'.jpg$'))
local_path = 'D:\pic'
for link in links :
    print(link.attrs['src'])
    request.urlretrieve(link.attrs['src'], local_path + r'\%s.jpg' % time.time())