# -*- coding:utf-8 -*-
#!usr/bin/env python
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 将本地的html加载到该对象中
    fp = open('./test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'xml')
    # print(soup.h1)
    # print(soup.find_all('h1'))
    print(soup.select('body'))
    print(soup.select('.tang > ul > li >a')[0]) # > 表示一个层级
    print(soup.select('.tang > ul a')[0]) # '' 表示多个层级
