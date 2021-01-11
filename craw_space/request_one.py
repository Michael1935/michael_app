# -*- coding:utf-8 -*-
#!usr/bin/env python
import requests

if __name__ == '__main__':
    url = 'https://www.sogou.com/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    page_text = response.text
    print(page_text)
    with open('./sougou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('over ')