# -*- coding:utf-8 -*-
#!usr/bin/env python
import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    params = {
        'type': '13',
        'interval_id': '100:90',
        'action':'',
        'start': '60',
        'limit': '20',
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }

    response = requests.get(url, params=params, headers=headers)
    list_data = response.json()
    print(list_data)
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('保存成功', 'over ')

    'git remote add origin git@github.com:wangyong315/python-crawl.git'