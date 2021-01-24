# -*- coding:utf-8 -*-
#!usr/bin/env python
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 将本地的html加载到该对象中
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    url='https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).text
    # 在首页中解析出章节的标题和详情页的url
    # 1 实例化一个Beautiful
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.text', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        detail_text = requests.get(url=detail_url, headers=headers).text
        detail_soup = BeautifulSoup(detail_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title + '爬取成功')
