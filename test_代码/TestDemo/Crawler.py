from urllib import request
from bs4 import BeautifulSoup
import re


class Crawler():
    # 抓取所有文本，传入抓取的URL，文件保存路径
    def crawlerAll(self, url, path):
        a = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        page = request.Request(url, headers=a)
        page_info = request.urlopen(page).read()
        b = BeautifulSoup(page_info, 'html.parser')
        print(b)
        pageFile = open(path, 'a', encoding = 'utf-8')
        pageFile.write(b.text)
        pageFile.close()

    # 抓取部分文本，传入抓取的URL，文件保存路径，抓取的标签，抓取的属性
    def crawlerWords(self, url, path, label, attribute):
        a = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        page = request.Request(url, headers=a)
        page_info = request.urlopen(page).read()
        b = BeautifulSoup(page_info, 'html.parser')
        pageFile = open(path, 'a')
        for j in b.find_all(label, attribute):
            print(j.text)
            pageFile.write(j.text)
        pageFile.close()

    # 抓取图片，传入抓取的URL，图片保存路径（路径必须已存在）
    def crawlerPicture(self, url, path):
        a = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        page = request.Request(url, headers=a)
        page_info = request.urlopen(page).read()
        b = BeautifulSoup(page_info, 'html.parser')
        print(b)
        soup = b.find_all('img', src=re.compile(r'.jpg$'))
        x = 0
        for img in soup:
            print(img.attrs['src'])
            request.urlretrieve(img.attrs['src'], path + r'\%s.jpg' % x)
            x += 1

url = 'https://s76k.chinaemail.cn/webmail7.5/webmail.php?r=site/index'
path = 'D:/pageCode.txt'
test = Crawler()
test.crawlerAll(url, path)
