# -*- coding:utf-8 -*-
#!usr/bin/env python
import requests
import re
import os


if __name__ == '__main__':
    if not os.path.exists('./qiutu_Images'):
        os.mkdir('./qiutuImgs')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    for page in range(1, 35):
        url = 'https://www.qiushibaike.com/imgrank/page/' + str(page)
        response = requests.get(url=url, headers=headers)
        pageText = response.text
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, pageText, re.S)
        for src in img_src_list:
            src = 'https:' + src
            img_data = requests.get(url=src, headers=headers).content
        #生成图片名称
            img_name = src.split('/')[-1]
            imgPath = './qiutuImgs/' + img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
                print(imgPath + 'is over')
